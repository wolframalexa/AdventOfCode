import copy
f = open("day5input.txt")
lines = f.readlines()

# create stacks
init_stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for line in lines[:8]:
	line = [line[i*4:(i+1)*4] for i in range((len(line) + 3) // 4)]
	for i in range(0,len(line)):
		if line[i] != "    " and line[i] != "   \n":
			init_stacks[i+1].append(''.join(c for c in line[i] if c.isalnum()))

stacks = copy.deepcopy(init_stacks)
stacks2 = copy.deepcopy(init_stacks)
# parse instructions
for instr in lines[10:]:
	instr = [int(s) for s in instr.split() if s.isdigit()]
	for i in range(1, instr[0]+1): # number of times to repeat
		crate = stacks[instr[1]].pop(0) # pop crate from origin
		stacks[instr[2]].insert(0, crate) # put crate on destination
print("After part 1:", stacks)

for instr in lines[10:]:
	instr = [int(s) for s in instr.split() if s.isdigit()]
	print(instr)
	crates = stacks2[instr[1]][:instr[0]] # get first n crates
	stacks2[instr[1]] = stacks2[instr[1]][instr[0]:] # remove those crates from the list
	stacks2[instr[2]] = crates + stacks2[instr[2]]
	print(stacks2)


print("After part 2:", stacks2)
