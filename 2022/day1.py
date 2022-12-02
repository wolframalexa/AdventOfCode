# part 1
f = open("day1input.txt", "r")
calories = f.read().split("\n\n")

max_cal = 0
cals = []
for elf in calories:
	carry = sum([int(i) for i in elf.split("\n") if i != ''])
	cals.append(carry)
	if carry > max_cal:
		max_cal = carry

print("Part 1 answer:", max_cal)


# part 2
cals.sort()
top3 = sum(cals[-3:])
print("Part 2 answer:", top3)
