f = open('day5input.txt', "r")
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


# PART 1
input = 5
i = 0
while i < len(numbers):
  instruction = f"{numbers[i]:05}"
  opcode = instruction[3:]
  mode1 = instruction[0]
  mode2 = instruction[1]
  mode3 = instruction[2]
  values = getValues(numbers, i, opcode, mode1, mode2, mode3)

  if opcode == "01":
    numbers[numbers[i+3]] = values[0] + values[1]
    i = i + 4

  elif opcode == "02":
    numbers[numbers[i+3]] = values[0] * values[1]
    i = i + 4

  elif opcode == "03":
    numbers[numbers[i+1]] = input
    i = i + 2

  elif opcode == "04":
    if values[0] != 0:
       print("The diagnostic code is: ", values[0])
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

  else:
    break

# part 2 was added to part 1 and the input changed



f.close()
