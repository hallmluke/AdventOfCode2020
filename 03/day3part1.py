file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

rows = []

for line in lines:
    row = []
    for c in line:
        row.append(c)
    rows.append(row)

curCol = 0
curRow = 0
trees = 0

while curCol < len(rows[0]) and curRow < len(rows):

    if(rows[curRow][curCol] == "#"):
        trees += 1
        rows[curRow][curCol] = "X"
    
    curCol += 3
    curRow += 1
    curCol = curCol % (len(rows[0]) - 1)

print(trees)
print(len(rows[0]))

for row in rows:
    print(''.join(row))