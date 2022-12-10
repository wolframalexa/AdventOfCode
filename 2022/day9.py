import numpy as np

def isAdjacent(x1,y1,x2,y2):
	# determines if head and tail are either colocated or adjacent
	return not ((abs(x1 - x2) > 1) or (abs(y1 - y2) > 1))

f = open("day9input.txt", "r")
instr = f.readlines()
instr = [x.strip("\n").split(" ") for x in instr]

# just make a big array
visited = np.zeros((1000,1000))


# for ease of numbering we'll start with (0,0). aoc has us start in position (dim,0)
# this means we'll need to adjust directions
# aoc's mapping | my mapping
# L	(-x)	| U (-y)
# R 	(+x)	| D (+y)
# U	(-y)	| R (+x)
# D	(+y)	| L (-x)

# initial state
headx = 0
heady = 0
tailx = 0
taily = 0

visited[heady,headx] = 1

for cmd in instr:
	for i in range(int(cmd[1])):
		# move head
		if cmd[0] == "R":
			heady += 1
			if not isAdjacent(headx,heady,tailx,taily):
				taily = heady - 1
				tailx = headx

		if cmd[0] == "L":
			heady -= 1
			if not isAdjacent(headx,heady,tailx,taily):
				taily = heady + 1
				tailx = headx

		if cmd[0] == "U":
			headx += 1
			if not isAdjacent(headx,heady,tailx,taily):
				tailx = headx - 1
				taily = heady

		if cmd[0] == "D":
			headx -= 1
			if not isAdjacent(headx,heady,tailx,taily):
				tailx = headx + 1
				taily = heady


		visited[:][taily,tailx] = 1

print("Part 1:", np.count_nonzero(visited))
