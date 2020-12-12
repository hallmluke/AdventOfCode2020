import string

f = open("testinput.txt", "r")
lines = f.readlines()
f.close()

count = 0
questions = set()

print(string.lowercase.index("c"))
print((1 << 26) - 1)

for line in lines:
    if line == "\n":
        print(len(questions))
        count += len(questions)
        questions = set()
        continue

    for c in line:       
        if c != "\n":
            print(c)
            questions.add(c)

if lines[-1] != "\n":
    count += len(questions)
    
print(count)