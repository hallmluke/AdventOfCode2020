import string

f = open("input.txt", "r")
lines = f.readlines()
f.close()

count = 0
questions = (1 << 26) - 1

print(string.lowercase.index("c"))
print((1 << 26) - 1)

for line in lines:
    if line == "\n":
        print("Group answer: " + str(bin(questions)))
        while questions > 0:
            count += questions & 1
            questions = questions >> 1
        questions = (1 << 26) - 1
        continue

    answered = 0
    for c in line:      
        if c != "\n":
            answered += 1 << string.lowercase.index(c)

    questions = questions & answered
    print(bin(questions))

if lines[-1] != "\n":
    while questions > 0:
        count += questions & 1
        questions = questions >> 1
    
print(count)