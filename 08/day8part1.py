file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

instructions = []
accumulator = 0

for line in lines:
    instructions.append(line)

pointer = 0
raninstructions = set()

while True:
    print(pointer)
    print(raninstructions)
    if pointer in raninstructions:
        print(accumulator)
        exit()
    raninstructions.add(pointer)
    instruction = instructions[pointer]
    parts = instruction.split()
    print(parts)
    if parts[0] == "nop":
        pointer += 1
    elif parts[0] == "acc":
        accumulator += int(parts[1])
        pointer += 1
    elif parts[0] == "jmp":
        pointer += int(parts[1])
    else:
        print("Something fucked up")
        exit()
    