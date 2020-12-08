file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

rows = []

for line in lines:
    row = []
    for c in line:
        row.append(c)
    rows.append(row)



vectors = [[1,1], [3,1], [5,1], [7,1], [1,2]]
vecTrees = []

for vec in vectors:
    curCol = 0
    curRow = 0
    trees = 0

    while curCol < len(rows[0]) and curRow < len(rows):

        if(rows[curRow][curCol] == "#"):
            trees += 1
    
        curCol += vec[0]
        curRow += vec[1]
        curCol = curCol % (len(rows[0]) - 1)

    print(trees)
    vecTrees.append(trees)

result = 1

for trees in vecTrees:
    result *= trees

print(result)

