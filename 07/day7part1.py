import re
from collections import deque

class Bag:
    def __init__(self):
        self.color = None
        self.contains = {}
        self.containedBy = set()

bags = {}

#newbag = Bag()

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

while len(bagstovisit) > 0:
    currentbag = bagstovisit.popleft()
    visitedbags.add(currentbag.color)
    for links in currentbag.containedBy:
        if links not in visitedbags:
            bagstovisit.append(bags.get(links))

print(visitedbags)
print(len(visitedbags))