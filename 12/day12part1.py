import math

f = open("input.txt", "r")
lines = f.readlines()
f.close()

rotation = 0
pos = [0,0]

for line in lines:
    action = line[0]
    print(action)
    value = int(line[1:])
    print(value)
    if action == "N":
        vec = [0,1 * value]
        pos = [x + y for x,y in zip(vec, pos)]
    elif action == "S":
        vec = [0,-1 * value]
        pos = [x + y for x,y in zip(vec, pos)]
    elif action == "E":
        vec = [1 * value,0]
        pos = [x + y for x,y in zip(vec, pos)]
    elif action == "W":
        vec = [-1 * value, 0]
        pos = [x + y for x,y in zip(vec, pos)]
    elif action == "L":
        rotation = rotation + value
    elif action == "R":
        rotation = rotation - value
    elif action == "F":
        vec = [math.cos(math.radians(rotation)) * value, math.sin(math.radians(rotation)) * value]
        pos = [x + y for x,y in zip(vec, pos)]
        
    print(pos)


print(pos)
print(math.fabs(pos[0]) + math.fabs(pos[1]))


