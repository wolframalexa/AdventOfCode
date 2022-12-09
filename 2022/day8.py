import numpy as np

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
print(trees2)

visible = np.zeros_like(trees2)

# from the left
for i in range(len(trees2)):
	highest = trees2[i][0]
	visible[:][i,0] = 1

	for j in range(len(trees2[i])):
		if trees2[i][j] > highest:
			visible[:][i,j] = 1
			highest = trees2[i][j]
# from the right
for i in range(len(trees2)):
	highest = trees2[i][-1]
	visible[:][i,-1] = 1

	for j in range(len(trees2[i],0)):

print(visible)
