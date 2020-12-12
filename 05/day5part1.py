f = open("input.txt", "r")
lines = f.readlines()
f.close()

high = 0
for boardingPass in lines:
    left = 0
    right = 128

    for i in range(0, 7):
        if boardingPass[i] == "F":
            right -= (right - left) / 2
        else:
            left += (right - left) / 2

    bottom = 0
    top = 8

    for i in range(0, 3):
        if boardingPass[i+7] == "R":
            bottom += (top - bottom) / 2
        else:
            top -= (top - bottom) / 2

    high = max(high, left * 8 + 5)

print(high)

