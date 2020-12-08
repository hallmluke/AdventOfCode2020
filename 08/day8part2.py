file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

instructions = []

for line in lines:
    instructions.append(line)



for i in range(0, len(instructions)):
    changedinstructions = instructions.copy()
    changed = instructions[i]
    split = changed.split()
    if split[0] == "nop":
        changedinstructions[i] = "jmp " + split[1]
    elif split[0] == "jmp":
        changedinstructions[i] = "nop " + split[1]

    accumulator = 0
    pointer = 0
    raninstructions = set()

    while pointer not in raninstructions:
        raninstructions.add(pointer)
        try:
            instruction = changedinstructions[pointer]
        except:
            break
        parts = instruction.split()

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
    
    if pointer == len(instructions):
        print("maybe this is right?")
        print(accumulator)