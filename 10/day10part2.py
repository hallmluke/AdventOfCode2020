file = open('input.txt', mode = 'r')
lines = file.readlines()
file.close()

def safe_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default
        
adapters = [0]
for line in lines:
    adapters.append(int(line))
adapters.sort()
jumps = [0] * (adapters[-1] + 1)
jumps[0] = 1
for i in range(1, len(adapters)):
    jumps[adapters[i]] = safe_get(jumps, adapters[i]-1, 0) + safe_get(jumps, adapters[i]-2, 0) + safe_get(jumps, adapters[i]-3, 0)

print(jumps)