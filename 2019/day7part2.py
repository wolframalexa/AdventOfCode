from itertools import permutations

f = open('day7input.txt', "r")
lines = f.readlines()
numbers = list(map(int, lines[0].split(',')))

class amplifier:
  def __init__(self, numbers):
    self.numbers = numbers[:]
    self.i = 0
    self.output = 0
    self.inputs = 0
    self.halt = False


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

def IntcodeComputer(amplifier, input, j):
  while amplifier.numbers[amplifier.i] != 99:
    instruction = f"{amplifier.numbers[amplifier.i]:05}"
    opcode = instruction[3:]
    mode1 = instruction[0]
    mode2 = instruction[1]
    mode3 = instruction[2]
    values = getValues(amplifier.numbers, amplifier.i, opcode, mode1, mode2, mode3)

    if opcode == "01":
      amplifier.numbers[amplifier.numbers[amplifier.i+3]] = values[0] + values[1]
      amplifier.i += 4

    elif opcode == "02":
      amplifier.numbers[amplifier.numbers[amplifier.i+3]] = values[0] * values[1]
      amplifier.i += 4

    elif opcode == "03":
      if not amplifier.inputs:
        amplifier.numbers[amplifier.numbers[amplifier.i+1]] = j
      else:
        amplifier.numbers[amplifier.numbers[amplifier.i+1]] = input

      amplifier.i += 2
      amplifier.inputs += 1

    elif opcode == "04":
      amplifier.output = values[0]
      amplifier.i += 2
      return amplifier

    elif opcode == "05":
      if values[0]:
        amplifier.i = values[1]
      else:
        amplifier.i += 3

    elif opcode == "06":
      if not values[0]:
        amplifier.i = values[1]
      else:
        amplifier.i += 3

    elif opcode == "07":
      if values[0] < values[1]:
        amplifier.numbers[amplifier.numbers[amplifier.i+3]] = 1
      else:
        amplifier.numbers[amplifier.numbers[amplifier.i+3]] = 0
      amplifier.i += 4

    elif opcode == "08":
      if values[0] == values[1]:
        amplifier.numbers[amplifier.numbers[amplifier.i+3]] = 1
      else:
        amplifier.numbers[amplifier.numbers[amplifier.i+3]] = 0
      amplifier.i += 4

  amplifier.halt = True
  return amplifier

# Part 2
maximum = 0

for list in permutations(range(5,10), 5):
  amps = [amplifier(numbers) for i in range(5)]
  active = 0

  while not amps[4].halt:
    amps[active] = IntcodeComputer(amps[active], amps[active-1].output, list[active])
    active = (active + 1) % 5

  maximum = max(maximum, amps[4].output)
print("The largest possible thrust (part 2) is: ", maximum)

f.close()
