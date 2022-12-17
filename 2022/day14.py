import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)


def moveSand(x,y,grid):
    # print("Current:", x, y)
    if grid[y+1,x] == 0: # try to move straight down
        # print('down')
        y += 1
        return moveSand(x,y,grid)
    elif grid[y+1, x-1] == 0: # try to move diagonally left
        # print('move left')
        y += 1
        x -= 1
        return moveSand(x,y,grid)
    elif grid[y+1, x+1] == 0: # try to move diagonally right
        # print("move right")
        y += 1
        x += 1
        return moveSand(x,y,grid)
    else: # no more moves possible
        return (x,y)

f = open("day14input.txt")

paths = f.readlines()
grid = np.zeros((172,130))
offset = 492

max_rock = 0
# make grid
for path in paths:
    i = 0

    coords = path.strip("\n").split(" -> ")
    coords = [[int(i) for i in xy.split(",")] for xy in coords]

    while i < len(coords) - 1:
        if coords[i][1] > max_rock:
            max_rock = coords[i][1]

        if coords[i][0] == coords[i+1][0]: # vertical line
            a = coords[i][1]
            b = coords[i+1][1]
            grid[:][min(a,b):max(a,b)+1, coords[i][0] - offset] = 1
        elif coords[i][1] == coords[i+1][1]: # horizontal line
            a = coords[i][0] - offset
            b = coords[i+1][0] - offset
            grid[:][coords[i][1], min(a,b):max(a,b)+1] = 1
        i += 1

print(max_rock)

# pour sand
startx = 500 - offset
starty = 0
sandx = startx
qty = 0
while True:
    try:
        (sandx, sandy) = moveSand(startx, starty, grid)
        grid[:][sandy, sandx] = 3
        qty += 1
    except:
        break
print("Part 1:", qty)

grid[:][max_rock + 2, :] = 1

startx = 500 - offset
starty = 0
sandx = 0
qty2 = 0
while True:
    (sandx, sandy) = moveSand(startx, starty, grid)
    # print(sandx,sandy)
    grid[:][sandy, sandx] = 3
    qty2 += 1
    if (sandx, sandy) == (500 - offset, 0):
        break
print("Part 2:", qty2)
