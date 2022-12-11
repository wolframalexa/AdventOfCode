f = open("day10input.txt","r")

cmd = f.readlines()

X = [1]
curr = 1
for line in cmd:
	line = line.strip("\n").split(" ")
	X.append(curr)

	if line[0] == "addx":
		X.append(curr)
		curr += int(line[1])

signals = X[20:-1:40]
weights = [20 + i * 40 for i in range(6)]

s = sum([signals[i] * weights[i] for i in range(len(signals))])
print("Part 1:", s)

# part 2
print("Part 2:")
row = ''
for i in range(1,len(X)):
	curr = X[i]
	sprite = [curr, curr+1, curr+2]

	if i%40 == 1:
		print(f'{row}')
		row = ''
	if i%40 in sprite:
		row += '#'
	else:
		row += '.'
print(row)
