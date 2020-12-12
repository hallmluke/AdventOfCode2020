import math

f = open("input.txt", "r")
lines = f.readlines()
f.close()

#rotation = 0
pos = [0,0]
waypoint = [10, 1]

for line in lines:
    action = line[0]
    print(action)
    value = int(line[1:])
    print(value)
    if action == "N":
        vec = [0,1 * value]
        waypoint = [x + y for x,y in zip(vec, waypoint)]
    elif action == "S":
        vec = [0,-1 * value]
        waypoint = [x + y for x,y in zip(vec, waypoint)]
    elif action == "E":
        vec = [1 * value,0]
        waypoint = [x + y for x,y in zip(vec, waypoint)]
    elif action == "W":
        vec = [-1 * value, 0]
        waypoint = [x + y for x,y in zip(vec, waypoint)]
    elif action == "L":
        s = math.sin(math.radians(value))
        c = math.cos(math.radians(value))
        waypoint = [waypoint[0] - pos[0], waypoint[1] - pos[1]]
        xnew = waypoint[0] * c - waypoint[1] * s
        ynew = waypoint[0] * s + waypoint[1] * c
        waypoint = [xnew + pos[0], ynew + pos[1]]
    elif action == "R":
        s = math.sin(math.radians(-value))
        c = math.cos(math.radians(-value))
        waypoint = [waypoint[0] - pos[0], waypoint[1] - pos[1]]
        xnew = waypoint[0] * c - waypoint[1] * s
        ynew = waypoint[0] * s + waypoint[1] * c
        waypoint = [xnew + pos[0], ynew + pos[1]]
    elif action == "F":
        vec = [waypoint[0] - pos[0], waypoint[1] - pos[1]]
        for i in range(0, value):
            pos = [pos[0] + vec[0], pos[1] + vec[1]]
        waypoint = [pos[0] + vec[0], pos[1] + vec[1]]
    print(waypoint)
    print(pos)


print(pos)
print(math.fabs(pos[0]) + math.fabs(pos[1]))


