f = open("day7input.txt")
cmd = f.readlines()

files = {}
path = []

for line in cmd:
    line = line.strip().split(" ")
    print(line)
    if line[1] == "cd":
        pass
    elif line[1] == "ls":
        pass
    elif line[0] == "dir":
        pass
    else: # size, file
        print("size, file")

# TODO add handling for each of the above cases