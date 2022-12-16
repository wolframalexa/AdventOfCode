def intToList(x):
    if isinstance(x,int):
        return [x]
    elif isinstance(x, list):
        return x

def compare(a, b):
    # returns 1 if items are in the right order
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    elif isinstance(a, list) and isinstance(b, list):
        if a == [] and b == []:
            return 0
        elif a == []:
            return 1
        elif b == []:
            return -1
            
        c = compare(a[0], b[0])
        if c == 0 and (len(a) > 1 or len(b) > 1):
            return compare(a[1:], b[1:])
        elif c == 1:
            return 1
        return c
    else: # exactly one is an integer, exactly one is a list
        return compare(intToList(a), intToList(b))

def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(a[j], a[j+1]) == -1:
                a[j], a[j+1] = a[j+1], a[j]
    # return a

f = open("day13input.txt")
pairs = [[eval(s) for s in pair.split('\n')] for pair in f.read().split("\n\n")]

i = 1
sum = 0
for pair in pairs:
    if compare(pair[0], pair[1]) == 1:
        sum += i
    i += 1
print("part 1:", sum)

# part 2: bubble sort go brrrr
f = open("day13input.txt")
pairs = f.readlines()

arr = []
for pair in pairs:
    if pair != "\n":
        arr.append(eval(pair.strip("\n")))
arr.append([[2]])
arr.append([[6]])

bubbleSort(arr)

key = (arr.index([[2]]) + 1) * (arr.index([[6]]) + 1)
print("Part 2:", key)