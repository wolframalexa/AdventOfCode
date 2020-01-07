from math import atan, degrees
from collections import defaultdict

# Get locations of all asteroids
def readFile(file):
  f = open(file, 'r')
  lines = f.readlines()

  i = 0
  asteroids = []
  for line in lines:
    for j in range(len(line)):
      if line[j] == "#":
        location = (i, j)
        asteroids.append(location)
    i += 1
  return asteroids

def gcd(x, y):
    if not x:
        return abs(y)
    if not y:
        return abs(x)
    
    while y:
        x, y = y, x % y
    return abs(x)

# find directions by which asteroids can be seen
def getDirections(station, asteroids):
  directions = set()
  for asteroid in asteroids:
    if asteroid == station:
      continue

    diff = (asteroid[0] - station[0], asteroid[1] - station[1])
    b = gcd(diff[0], diff[1])
    diff = (diff[0] // b, diff[1] // b)

    directions.add(diff)
  return directions


def angle(vector):
  if vector[1] == 0:
    return 90
  angle = degrees(atan(vector[0]/vector[1]))
  return angle


def findQuadrants(asteroids):
  quadrants = []
  quadrants.append([x for x in directions if x[0] >= 0 and x[1] < 0])
  quadrants.append([x for x in directions if x[0] > 0  and x[1] >= 0])
  quadrants.append([x for x in directions if x[0] <= 0 and x[1] > 0])
  quadrants.append([x for x in directions if x[0] < 0  and x[1] <= 0])
  return quadrants

def vaporize(quadrants, station, asteroids):
  vaporized = 0

  while True:
    for quadrant in quadrants:
      for direction in quadrant:
        m = 1
        while True:
          coord = (station[0] + direction[0]*m, station[1] + direction[1]*m)
          if coord[0] < 0 or coord[0] > 21 or coord[1] < 0 or coord[1] > 21:
            break

          if coord in asteroids:
            asteroids.remove(coord)
            vaporized += 1

            if vaporized == 201: # off by one errors are fun!
              return coord[0]*100 + coord[1]
            break
          m += 1

# Part 1
asteroids = readFile("day10input.txt")
lens = []

f = open("day10input.txt", 'r')
lines = f.readlines()

for station in asteroids:
  directions = getDirections(station, asteroids)
  lens.append(len(directions))
maximum = max(lens)

print("The most asteroids that can be observed are: ", maximum)

# Part 2: inspired by @dementophobia's solution
best = asteroids[lens.index(maximum)]
directions = list(getDirections(best, asteroids))
directions.sort(key = lambda direction:angle(direction), reverse = True)

quadrants = findQuadrants(directions)

final = vaporize(quadrants, best, asteroids)
print("Final result for part 2: ", final)
