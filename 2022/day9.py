import numpy as np

def isAdjacent(x1,y1,x2,y2):
	# determines if head and tail are either colocated or adjacent
	return not ((abs(x1 - x2) > 1) or (abs(y1 - y2) > 1))

def moveRope(dir,x1,y1,x2,y2):
	if dir == "R":
		y1 += 1
		if not isAdjacent(x1,y1,x2,y2):
			y2 = y1 - 1
			x2 = x1

	if dir == "L":
		y1 -= 1
		if not isAdjacent(x1,y1,x2,y2):
			y2 = y1 + 1
			x2 = x1

	if dir == "U":
		x1 += 1
		if not isAdjacent(x1,y1,x2,y2):
			x2 = x1 - 1
			y2 = y1

	if dir == "D":
		x1 -= 1
		if not isAdjacent(x1,y1,x2,y2):
			x2 = x1 + 1
			y2 = y1

	return((x1,y1),(x2,y2))

f = open("day9test.txt", "r")
instr = f.readlines()
instr = [x.strip("\n").split(" ") for x in instr]

# just make a big array
visited = np.zeros((10,10))


# for ease of numbering we'll start with (0,0). aoc has us start in position (dim,0)
# this means we'll need to adjust directions
# aoc's mapping | my mapping
# L	(-x)	| U (-y)
# R 	(+x)	| D (+y)
# U	(-y)	| R (+x)
# D	(+y)	| L (-x)

# initial state
(headx, heady) = (0,0)
(tailx, taily) = (0,0)

visited[heady,headx] = 1

for cmd in instr:
	for i in range(int(cmd[1])):
		new = moveRope(cmd[0], headx, heady, tailx, taily)
		(headx, heady) = new[0]
		(tailx, taily) = new[1]
		visited[:][taily,tailx] = 1

print("Part 1:", np.count_nonzero(visited))

# part 2: extend the above to 10 knots
knots = [(0,0) for i in range(10)]

visited2 = np.zeros((10,10))

for cmd in instr:
	for i in range(int(cmd[1])):
		for j in range(9):
			new = moveRope(cmd[0], knots[j][0], knots[j][1], knots[j+1][0], knots[j+1][1])
			knots[j] = new[0]
			knots[j+1] = new[1]
		visited[:][knots[9][1], knots[9][0]] = 1
	print(knots)
print(visited2)
# do everything the same as above except recursively
# eg knot 1 is the tail of knot 0, knot 2 is the tail of knot 1, etc
