from itertools import permutations

f = open('day7input.txt', "r")
lines = f.readlines()
numbers = list(map(int, lines[0].split(',')))

def getValues(input, pos, opcode, mode1, mode2, mode3):
  values = []
  if opcode in ["01", "02", "04", "05", "06", "07", "08"]:
    if mode3 == "0":
      values.append(input[input[pos+1]])
    else:
      values.append(input[pos+1])

    if opcode in ["01", "02", "05", "06", "07", "08"]:
      if mode2 == "0":
        values.append(input[input[pos+2]])
      else:
        values.append(input[pos+2])

      if opcode in []:
        if mode1 == "0":
          values.append(input[input[pos+3]]) # parameters that an instruction writes to are never in immediate mode
        else:
          values.append(input[pos+3])
  return values

def IntcodeComputer(numbers, input, j, halt):
  i = 0
  inputs = 0

  while numbers[i] != 99:
    instruction = f"{numbers[i]:05}"
    opcode = instruction[3:]
    mode1 = instruction[0]
    mode2 = instruction[1]
    mode3 = instruction[2]
    values = getValues(numbers, i, opcode, mode1, mode2, mode3)

    print(opcode)
    if opcode == "01":
      numbers[numbers[i+3]] = values[0] + values[1]
      i = i + 4

    elif opcode == "02":
      numbers[numbers[i+3]] = values[0] * values[1]
      i = i + 4

    elif opcode == "03":
      if not inputs:
        numbers[numbers[i+1]] = j
      else:
        numbers[numbers[i+1]] = input
      i = i + 2
      inputs = inputs + 1

    elif opcode == "04":
      output = values[0]
      i = i + 2

    elif opcode == "05":
      if values[0]:
        i = values[1]
      else:
        i = i + 3

    elif opcode == "06":
      if not values[0]:
        i = values[1]
      else:
        i = i + 3

    elif opcode == "07":
      if values[0] < values[1]:
        numbers[numbers[i+3]] = 1
      else:
        numbers[numbers[i+3]] = 0
      i = i + 4

    elif opcode == "08":
      if values[0] == values[1]:
        numbers[numbers[i+3]] = 1
      else:
        numbers[numbers[i+3]] = 0
      i = i + 4

  halt = True
  return output

# Part 1
maximum = 0
halt = False
for list in permutations(range(5), 5):
  output = 0

  for i in list:
    output = IntcodeComputer(numbers, output, i, halt)
  maximum = max(maximum, output)

print("The largest possible thrust (part 1) is: ", maximum)
f.close()
