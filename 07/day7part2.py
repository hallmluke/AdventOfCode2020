import re
from collections import deque

class Bag:
    def __init__(self):
        self.color = None
        self.contains = {}
        self.containedBy = set()

bags = {}

#newbag = Bag()
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total

def dfs(bags, bag, factors):
    childnums = 0
    for color, num in bag.contains.items():
        newfactors = factors.copy()
        newfactors.append(int(num))
        childnums += dfs(bags, bags.get(color), newfactors)
    print(bag.color)
    print(factors)
    return childnums + multiply(factors)


file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

for teststring in lines:
    key = re.match("^(.*)\sbags\scontain", teststring)
    remainder = teststring.split("contain", 1)[1]

    newbag = bags.get(key.groups()[0])
    if newbag is None:
        newbag = Bag()
        newbag.color = key.groups()[0]

    splitvalues = remainder.split(",")

    for value in splitvalues:
        values = re.match("\s?([1-9])\s(.*)\sbag", value)
        
        if values:
            newbag.contains[values[2]] = values[1]

            containedBag = bags.get(values[2])
            if containedBag is None:
                containedBag = Bag()
            containedBag.color = values[2]
            containedBag.containedBy.add(newbag.color)
            bags[containedBag.color] = containedBag

    bags[newbag.color] = newbag

for color, bag in bags.items():
    print(bag.color)
    print(bag.contains)
    print(bag.containedBy)

visitedbags = set()
currentbag = bags["shiny gold"]
bagstovisit = deque()
bagstovisit.append(currentbag)
count = 0

while len(bagstovisit) > 0:
    currentbag = bagstovisit.popleft()
    visitedbags.add(currentbag.color)
    for bagcolor, num in currentbag.contains.items():
        if bagcolor not in visitedbags:
            bagstovisit.append(bags.get(bagcolor))
            count += int(num)



print(visitedbags)
print(len(visitedbags))
print(count)

print(dfs(bags, bags.get("shiny gold"), [1]))