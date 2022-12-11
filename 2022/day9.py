import numpy as np
import sys
#np.set_printoptions(threshold=sys.maxsize)

def isDirectMove(x1,y1,x2,y2):
	# tail directly follows head bc they are in the same row or column
	return (((x1 == x2) or (y1 == y2)) and ((abs(x1 - x2) > 1) or (abs(y1 -y2) > 1)))

def isDiagMove(x1,y1,x2,y2):
	# determines if tail needs to follow diagonally
	return ((x1 != x2) and (y1 != y2) and ((abs(x1 - x2) > 1) or (abs(y1 - y2) > 1)))

def moveRope(dir,x1,y1,x2,y2):
	if dir == "R":
		y1 += 1
	if dir == "L":
		y1 -= 1
	if dir == "U":
		x1 += 1
	if dir == "D":
		x1 -= 1

	return (x1,y1)

def updateTail(dir, x1, y1, x2, y2):
	if isDiagMove(x1,y1,x2,y2):
		if abs(x1 - x2) == 1:
			x2 = x1
			if y1 > y2:
				y2 += 1
			elif y2 > y1:
				y2 -= 1
		else:
			y2 = y1
			if x1 > x2:
				x2 += 1
			elif x2 > x1:
				x2 -= 1

	elif isDirectMove(x1,y1,x2,y2):
		if x1 == x2: # if the same in x
			if y1 > y2:
				y2 += 1
			elif y2 > y1:
				y2 -= 1
		elif y1 == y2: # if the same in y
			if x1 > x2:
				x2 += 1
			elif x2 > x1:
				x2 -= 1
	return (x2,y2)


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
(headx, heady) = (0,0)
(tailx, taily) = (0,0)

visited[heady,headx] = 1

for cmd in instr:
	for i in range(int(cmd[1])):
		(headx, heady) = moveRope(cmd[0], headx, heady, tailx, taily)
		(tailx, taily) = updateTail(cmd[0], headx, heady, tailx, taily)
		visited[:][taily,tailx] = 1

print("Part 1:", np.count_nonzero(visited))

# part 2: extend the above to 10 knots
knots = [(0,0) for i in range(10)]

visited2 = np.zeros((1000,1000))
mid = 500

for cmd in instr:
	for i in range(int(cmd[1])):
		knots[0] = moveRope(cmd[0], knots[0][0], knots[0][1], knots[1][0], knots[1][1])
		for j in range(9):
			knots[j+1] = updateTail(cmd[0], knots[j][0], knots[j][1], knots[j+1][0], knots[j+1][1])
			visited2[:][knots[9][1] + mid, knots[9][0] + mid] = 1
print("Part 2:",np.count_nonzero(visited2))
# do everything the same as above except recursively
# eg knot 1 is the tail of knot 0, knot 2 is the tail of knot 1, etc
