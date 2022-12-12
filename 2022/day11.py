import re
import math
import copy


class Monkey:
    def __init__(self, items, num, op, test, t_recip, f_recip):
        self.items = items
        self.num = num
        self.op = op # stores operation
        self.test = test
        self.t_recip = t_recip # recipient if true
        self.f_recip = f_recip # recipient if true

def doRound(monkeys, div):
    for j in range(len(monkeys)):
        curr = monkeys[j]
        for old in curr.items:
            curr.num += 1
            worry = math.floor(eval(curr.op) // div)
            curr.items = curr.items[1:]
            if worry % curr.test == 0:
                monkeys[curr.t_recip].items.append(worry)
            else:
                monkeys[curr.f_recip].items.append(worry)
    # find two most active monkeys
    nums = []
    for monkey in monkeys:
        nums.append(monkey.num)
    nums.sort()
    return(nums[-2] * nums[-1])

def doRound2(monkeys, modulo):
    for curr in monkeys:
        for old in curr.items:
            curr.num += 1
            worry = eval(curr.op) % modulo
            curr.items = curr.items[1:]

            if worry % curr.test == 0:
                monkeys[curr.t_recip].items.append(worry)
            else:
                monkeys[curr.f_recip].items.append(worry)
    return(monkeys)
    
# parse input to create monkeys
f = open("day11input.txt", "r")
monkeys = f.read().split("\n\n")

objs = []
for m in monkeys:
    m = m.split("\n")
    it = [int(s) for s in re.findall(r'\d+', m[1])]
    op = m[2][18:]
    t = int(re.findall(r'\d+', m[3])[0])
    tr = int(m[4][-1])
    fr = int(m[5][-1])

    newmonk = Monkey(it, 0, op, t, tr, fr)
    objs.append(newmonk)

objs2 = copy.deepcopy(objs)

# monkeys doing monkey business
for i in range(20): # 20 rounds
    business = doRound(objs,3)
    # loop through monkeys updating their holdings
print("Part 1:", business)


z = math.prod(m.test for m in objs)
for i in range(10000):
    objs2 = doRound2(objs2,z)

nums = []
for monkey in objs2:
    nums.append(monkey.num)
nums.sort()
print("Part 2:", nums[-2] * nums[-1])
    