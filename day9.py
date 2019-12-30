from collections import defaultdict

f = open('day9input.txt', "r")
lines = f.readlines()
numbers = list(map(int, lines[0].split(',')))

class Booster:
  def __init__(self, numbers):
    self.numbers = numbers
    self.i = 0
    self.output = 0
    self.relbase = 0

def createProgram(input):
  numbers = defaultdict(int)
  for i in range(len(input)):
    numbers[i] = int(input[i])
  return numbers

def getValues(input, pos, opcode, mode1, mode2, mode3, booster):
  values = []
  offset = 0

  if opcode in ["01", "02", "04", "05", "06", "07", "08", "09"]:
    if mode3 == "0":
      values.append(input[input[pos+1]])
    elif mode3 == "1":
      values.append(input[pos+1])
    elif mode3 == "2":
      values.append(input[input[pos+1]+ booster.relbase])

    if opcode in ["01", "02", "05", "06", "07", "08"]:
      if mode2 == "0":
        values.append(input[input[pos+2]])
      elif mode2 == "1":
        values.append(input[pos+2])
      elif mode2 == "2":
        values.append(input[input[pos+2]+ booster.relbase])

      if opcode in []:
        if mode1 == "0":
          values.append(input[input[pos+3]]) # parameters that an instruction writes to are never in immediate mode
        elif mode1 == "1":
          values.append(input[pos+3])
        else:
          values.append(input[input[pos+2]+ booster.relbase])

  if opcode in ["01", "02", "07", "08"]:
    if mode1 == "2":
      offset = booster.relbase

  if opcode in ["03"]:
    if mode3 == "2":
      offset = booster.relbase

  return values, offset

def IntcodeComputer(input, booster):
  while booster.numbers[booster.i] != 99:
    instruction = f"{booster.numbers[booster.i]:05}"
    opcode = instruction[3:]
    mode1 = instruction[0]
    mode2 = instruction[1]
    mode3 = instruction[2]
    values, offset = getValues(booster.numbers, booster.i, opcode, mode1, mode2, mode3, booster)

    if opcode == "01":
      booster.numbers[booster.numbers[booster.i+3] + offset] = values[0] + values[1]
      booster.i += 4

    elif opcode == "02":
      booster.numbers[booster.numbers[booster.i+3] + offset] = values[0] * values[1]
      booster.i += 4

    elif opcode == "03":
      booster.numbers[booster.numbers[booster.i+1] + offset] = input
      booster.i += 2

    elif opcode == "04":
      booster.output = values[0]
      booster.i += 2

    elif opcode == "05":
      if values[0]:
        booster.i = values[1]
      else:
        booster.i += 3

    elif opcode == "06":
      if not values[0]:
        booster.i = values[1]
      else:
        booster.i += 3

    elif opcode == "07":
      if values[0] < values[1]:
        booster.numbers[booster.numbers[booster.i+3] + offset] = 1
      else:
        booster.numbers[booster.numbers[booster.i+3] + offset] = 0
      booster.i += 4

    elif opcode == "08":
      if values[0] == values[1]:
        booster.numbers[booster.numbers[booster.i+3] + offset] = 1
      else:
        booster.numbers[booster.numbers[booster.i+3] + offset] = 0
      booster.i += 4

    elif opcode == "09":
      if len(values) != 0:
        booster.relbase += values[0]
      booster.i += 2

  return booster


# Part 1
numbers = createProgram(numbers)
booster = Booster(numbers)
IntcodeComputer(1, booster)
print("The booster output for part 1 is: ", booster.output)


# Part 2
booster = Booster(numbers)
IntcodeComputer(2, booster)
print("The distress signal is: ", booster.output)

f.close()
