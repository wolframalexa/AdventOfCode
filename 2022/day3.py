from string import ascii_letters
f = open("day3input.txt")

rucksacks = f.readlines()

# part 1
items = []
for sack in rucksacks:
	sack = sack[:-1]
	l = len(sack)//2
	same = set(sack[:l]) & set(sack[l:])
	items.append(list(same)[0])

priority = sum(ascii_letters.index(letter) + 1 for letter in items)
print("Part 1: ", priority)

# part 2
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

badges = []
for group in groups:
	same = set(group[0][:-1]) & set(group[1][:-1]) & set(group[2][:-1])
	badges.append(list(same)[0])
print(badges)
priority = sum(ascii_letters.index(letter) + 1 for letter in badges)
print("Part 2: ", priority)
