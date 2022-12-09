import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def findVisible(trees):
	visible = np.zeros_like(trees)
	for i in range(len(trees)):
		highest = trees[i][0]
		visible[:][i,0] = 1

		for j in range(len(trees2[i])):
			if trees2[i][j] > highest:
				visible[:][i,j] = 1
				highest = trees2[i][j]
	return(visible)

f = open("day8input.txt", "r")

trees = f.readlines()

trees2 = []
for row in trees:
	row = row.strip("\n")
	trees2.append([int(x) for x in [*row]])
trees2 = np.array(trees2)

# from the left
left_vis = findVisible(trees2)

# from the right
right_vis = findVisible(np.fliplr(trees2))

# from the bottom
bottom_vis = findVisible(np.transpose(trees2))

# from the bottom
top_vis = findVisible(np.fliplr(np.transpose(trees2)))

vis = left_vis + np.fliplr(right_vis) + np.transpose(top_vis) + np.transpose(np.fliplr(bottom_vis))
#print(vis)
print(np.count_nonzero(vis))
