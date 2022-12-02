f = open("day2input.txt", "r")
plays = f.read().split("\n")

vals = dict({"X": 1, "Y": 2, "Z": 3})
score = 0

for play in plays[:-1]:
	play = play.split(" ")
	score += vals[play[1]]
	if (play[0] == 'A' and play[1] == 'Y') or (play[0] == 'B' and play[1] == 'Z') or (play[0] == 'C' and play[1] == 'X'): # I win
		score += 6
	elif (play[0] == 'A' and play[1] == 'Z') or (play[0] == 'B' and play[1] == 'X') or (play[0] == 'C' and play[1] == 'Y'): # opponent wins
		pass
	else: # draw
		score += 3

print("Part 1:", score)

# part 2
elf_vals = dict({"A":1, "B":2, "C":3})
score = 0

for play in plays[:-1]:
	play = play.split(" ")
	if play[1] == "Z": # win
		if play[0] == "A":
			score += vals["Y"]
		elif play[0] == "B":
			score += vals["Z"]
		else:
			score += vals["X"]
		score += 6
	elif play[1] == "X": # lose
		if play[0] == "A":
			score += vals["Z"]
		elif play[0] == "B":
			score += vals["X"]
		else:
			score += vals["Y"]
	else: # draw
		score += 3
		score += elf_vals[play[0]]
print("Part 2:", score)
