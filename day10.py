
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


# Part 1
asteroids = readFile("day10input.txt")
lens = []

for station in asteroids:
  directions = getDirections(station, asteroids)
  lens.append(len(directions))
maximum = max(lens)

print("The most asteroids that can be observed are: ", maximum)

# Part 2
best = asteroids.index(maximum)
