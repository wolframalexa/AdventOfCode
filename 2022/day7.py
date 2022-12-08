from collections import defaultdict

f = open("day7input.txt")
cmd = f.readlines()

files = defaultdict(int)
path = []

for line in cmd:
	line = line.strip().split(" ")
	if line[1] == "cd":
		if line[2] == "..":
			path.pop()
		elif line[2] == "/":
			path = ["/"]
		else:
			path.append(line[2])
	elif line[1] == "ls":
		pass
	elif line[0] == "dir":
		pass
	else: # size, file
		for i in range(len(path)):
			k = "/".join(path[:i+1])
			files[k] += int(line[0])

new = dict(filter(lambda files: files[1] <= 100000, files.items()))
print("Part 1:", sum(new.values()))

target = 30000000 - (70000000 - files["/"])
todelete = min(dict(filter(lambda files: files[1] > target, files.items())).values())
print("Part 2:", todelete)
