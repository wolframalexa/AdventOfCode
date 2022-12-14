def intToList(x):
    if isinstance(x,int):
        return [x]
    elif isinstance(x, list):
        return x

def compare(a, b):
    print("Comparing:", a, "vs", b)
    # returns true if items are in the right order
    if isinstance(a, int) and isinstance(b, int):
        print("both ints")
        if a < b:
            print('smaller!')
            return True
        else:
            return False
    elif isinstance(a, list) and isinstance(b, list):
        print('both lists')
        c = compare(a[0], b[0])
        if c == False and len(a) > 1:
            return compare(a[1:], b[1:])
        return c
        # if len(a) < len(b):
        #     return True
    else: # exactly one is an integer, exactly one is a list
        print("mixed")
        compare(intToList(a), intToList(b))

f = open("day13test.txt")
pairs = [[eval(s) for s in pair.split('\n')] for pair in f.read().split("\n\n")]

i = 1
sum = 0
for pair in pairs[1:2]:
    print(pair)
    print(compare(pair[0], pair[1]))
    if compare(pair[0], pair[1]):
        sum += i
        print("new correct pair, index", i, sum)
    i += 1
print("pairs in correct order:", sum)