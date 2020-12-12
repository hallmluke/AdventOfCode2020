f = open("input.txt", "r")
lines = f.readlines()
f.close()

high = 0
ids = set()
seats = []

for i in range(0, 128):
    new = []
    for j in range (0, 8):
        new.append(0)
    seats.append(new)

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

    seatid = left * 8 + bottom
    ids.add(seatid)
    seats[left][bottom] = 1

for i in range(0, 128):
    for j in range (0, 8):
        if seats[i][j] == 0:
            #print(str(i) + ", " + str(j))
            openid = i * 8 + j
            if openid - 1 in ids and openid + 1 in ids:
                print openid


