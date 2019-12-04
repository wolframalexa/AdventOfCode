from collections import defaultdict

f = open('day3input.txt', "r")
lines = f.readlines()
firstwire = map(str, lines[0].split(','))
secondwire = map(str, lines[1].split(','))

ManhattanDistances = []
WireDistances = []

# sets the path of the wires
def followCommand(instructions):
  xpos,ypos = 0,0
  positions = set()

  for i in instructions:
    for j in range(int(i[1:])):
      direction = i[0]
      if direction == "R":
        xpos = xpos + 1
      elif direction == "L":
        xpos = xpos - 1
      elif direction == "U":
        ypos = ypos + 1
      elif direction == "D":
        ypos = ypos - 1
      positions.add((xpos,ypos))
  return positions

# find Manhattan distance between an intersection and the origin
def findManhattanDistance(position):
    x = abs(position[0])+abs(position[1])
    if x != 0:
      ManhattanDistances.append(x)

# Find distance it takes to get to an intersection
def crossingDistance(instructions, crossings):
  distance = 0
  xpos,ypos = 0,0
  crossingDistances = defaultdict(int)

  for i in instructions:
    for j in range(int(i[1:])):
      direction = i[0]
      if direction == "R":
        xpos = xpos + 1
      elif direction == "L":
        xpos = xpos - 1
      elif direction == "U":
        ypos = ypos + 1
      elif direction == "D":
        ypos = ypos - 1
      distance = distance + 1
      if (xpos,ypos) in crossings:
        crossingDistances[(xpos,ypos)] = distance
  return crossingDistances


# Part 1
wire1 = followCommand(firstwire)
wire2 = followCommand(secondwire)

crossings = wire1.intersection(wire2) # cool property of sets!

for pos in crossings:
  findManhattanDistance(pos)
minDistance = min(ManhattanDistances)
print "The minimal distance in part 1 is: ",minDistance


# Part 2
wire1distances = crossingDistance(firstwire,crossings)
wire2distances = crossingDistance(secondwire,crossings)

for i in crossings:
  WireDistances.append(wire1distances[i]+wire2distances[i])
minWireDistance = min(WireDistances)
print "The minimal distance for part 2 is: ",minWireDistance
