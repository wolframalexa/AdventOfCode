import numpy as np

def score2(data,h,flip=False):
	try:
		if len(data) > 1 and flip:
			data = data[::-1]
	except:
		pass
	x = np.where(data>=h)[0]
	if x.size != 0:
		return x[0]+1
	try:
		return len(data)
	except:
		return 1

def score(data,x,y):
	a = 0
	b = 0
	c = 0
	d = 0

	h = data[x,y]
	a = score2(data[x+1:,y].squeeze(),h)
	b = score2(data[:x,y].squeeze(),h,True)
	c = score2(data[x,y+1:].squeeze(),h)
	d = score2(data[x,:y:].squeeze(),h,True)
	return a*b*c*d

def findVisible(data):
	visible = np.zeros_like(data)
	for i in range(len(data)):
		highest = data[i][0]
		visible[:][i,0] = 1

		for j in range(len(data[i])):
			if data[i][j] > highest:
				visible[:][i,j] = 1
				highest = data[i][j]
	return visible

f = open("day8input.txt", "r")
trees = f.readlines()

trees2 = []
for row in trees:
	row = row.strip("\n")
	trees2.append([int(x) for x in [*row]])
trees2 = np.array(trees2)
high = 0
best = 0
for i in range(trees2.shape[0]):
	for j in range(trees2.shape[1]):
		n = score(trees2,i,j)
		if n > high:
			best = (i,j)
			high = n
print(best)
print("Part 2:", high)

# from the left
left_vis = findVisible(trees2)

# from the right
right_vis = findVisible(np.fliplr(trees2))

# from the top
top_vis = findVisible(np.rot90(trees2))

bottom_vis = findVisible(np.fliplr(np.rot90(trees2)))
# from the bottom
vis = left_vis + np.fliplr(right_vis) + np.fliplr(np.rot90(bottom_vis)) + np.fliplr(np.rot90(np.fliplr(top_vis)))
print("Part 1:", np.count_nonzero(vis))
