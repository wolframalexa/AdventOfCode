from collections import defaultdict

f = open('day8input.txt', "r")
line = f.readlines()
line = line[0][:-1]

# Part 1

# Find layers
i = 0
layers = defaultdict(list)
size = 25 * 6

layercounter = -1

for digit in line:
  if not i % size:
    layercounter += 1

  layers[layercounter].append(int(digit))
  i += 1

# Find layer with smallest number of zeros
minzeros = 100000
smallestlayer = 0
for layer in layers:
  current = 0
  for digit in layers[layer]:
    if digit == 0:
      current += 1

  minzeros = min(minzeros, current)
  if minzeros == current:
    smallestlayer = layer

# Find number of ones and twos in that layer
numones = 0
numtwos = 0
for digit in layers[smallestlayer]:
  if digit == 1:
    numones += 1
  if digit == 2:
    numtwos += 1
result = numones * numtwos
print("Answer for part 1: ", result)


# Part 2
# Create lists for each position
positions = defaultdict(list)
for layer in layers:
  for i in range(len(layers[layer])):
    positions[i].append(layers[layer][i])

#iterate through positions to find colour of each pixel
image = []
for pixel in positions:
  count = 0
  for i in positions[pixel]:
    if i == 1:
      image.append("#")
      break
    if i == 0:
      image.append(" ")
      break
  count += 1

# Print image to reveal message
print("Message revealed in part 2:")

i = 0
length = 25
for j in range(len(image)):
  if i % length == 0:
    print("")
  print(image[i], end="")
  i += 1
print("\n")
