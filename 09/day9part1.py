from collections import deque

size = 25

numberqueue = deque(maxlen=size)

f = open("input.txt", "r")
lines = f.readlines()
f.close()

index = 0
for line in lines:
    foundPair = False
    if index >= size:
        currentset = set(numberqueue)
        for num in currentset:
            if (int(line) - num) in currentset and (int(line) - num) != int(line):
                foundPair = True
                break 
        
        if foundPair == False:
            invalid = int(line)
            break

    numberqueue.append(int(line))
    index += 1

leftpointer = 0
rightpointer = 1
currentsum = int(lines[leftpointer]) + int(lines[rightpointer])

while currentsum != invalid or leftpointer >= rightpointer:
    if currentsum > invalid:
        currentsum -= int(lines[leftpointer])
        leftpointer += 1
    elif currentsum <= invalid:
        rightpointer += 1
        currentsum += int(lines[rightpointer])

minimum = float('inf')
maximum = float('-inf')

while leftpointer <= rightpointer:
    minimum = min(minimum, int(lines[leftpointer]))
    maximum = max(maximum, int(lines[leftpointer]))
    leftpointer += 1

print(minimum)
print(maximum)
print(minimum + maximum)