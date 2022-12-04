f = open("day4input.txt")
pairs = f.readlines()

cont = 0
over = 0
for pair in pairs:
	pair = pair[:-1].split(",")
	elf1 = [int(i) for i in pair[0].split("-")]
	elf2 = [int(i) for i in pair[1].split("-")]

	if (elf1[0] >= elf2[0]) and (elf1[1] <= elf2[1]): # elf 1 contained in elf 2
		cont += 1
		over += 1
	elif (elf2[0] >= elf1[0]) and (elf2[1] <= elf1[1]): # elf 2 contained in elf 1
		cont += 1
		over += 1
	elif not ((elf1[0] > elf2[1]) or (elf2[0] > elf1[1])):
		over += 1
	else: # not contained, not overlapping
		pass
print("part 1:", cont)
print("part 2:", over)

