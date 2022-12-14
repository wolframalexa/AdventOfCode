import numpy as np

f = open("day12input.txt", "r")
lines = f.readlines()

el = []
for line in lines:
    el.append([*line.strip("\n")])
el = np.array(el)

# find start & end
start = np.where(el == "S")
end = np.where(el == "E")[0]

print(start, end)