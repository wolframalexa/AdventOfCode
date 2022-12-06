f = open("day6input.txt")
comms = f.read()

marker = 0
for i in range(0, len(comms)-4):
    seq = comms[i:i+4]
    if len(seq) == len(set(seq)): # not the same
        marker = i+4
        break
print("Part 1:", marker)

for i in range(0, len(comms)-14):
    seq = comms[i:i+14]
    if len(seq) == len(set(seq)): # not the same
        marker = i+14
        break
print("Part 2:", marker)