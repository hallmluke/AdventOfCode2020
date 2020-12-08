import re

file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

lowerbounds = []
upperbounds = []
letters = []
passwords = []

for line in lines:
    x = line.split()
    bounds = re.match("(\d{1,2})-(\d{1,2})", x[0])
    lowerbounds.append(bounds[1])
    upperbounds.append(bounds[2])
    letters.append(x[1][0])
    passwords.append(x[2])
    print(bounds[1] + "-" + bounds[2] + " " + x[1][0] + ": " + x[2])

valid = 0

for i in range(0, len(passwords)):
    num = 0
    for c in passwords[i]:
        if c == letters[i]:
            num += 1

    if num >= int(lowerbounds[i]) and num <= int(upperbounds[i]):
        valid += 1

print(valid)