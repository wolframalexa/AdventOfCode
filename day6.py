f = open('day6input.txt', "r")
input = f.readlines()

def FindOrbits(input):
  orbits = {}
  for line in input:
    planets = line.split(")")
    orbits[planets[1][:3]] = planets[0] # key is orbiter planet, entry is orbited, need to remove \n from entry
  return orbits

def FindDepth(orbits, planet):
  i = 0
  while planet in orbits.keys():
    planet = orbits[planet]
    i = i + 1
  return i

def GetPlanets(input):
  allplanets = []
  for line in input:
    planets = line.split(")")
    if planets[0] not in allplanets:
      allplanets.append(planets[0])
    if planets[1][:3] not in allplanets: # need to remove \n, results in not being counted
      allplanets.append(planets[1][:3])
  return allplanets

# Part 1
orbits = FindOrbits(input)
all = GetPlanets(input)

sum = 0
for i in all:
  sum = sum + FindDepth(orbits, i)

print("There are ", sum, " indirect and direct orbits in part 1")

# Part 2
# this is a tree: find the depth between YOU and SAN and their closest common ancestor

def FindAncestors(planet):
  ancestors = []
  pos = planet
  while pos != "COM":
    pos = orbits[pos]
    ancestors.append(pos)
  return ancestors

YOUAncestors = set(FindAncestors("YOU"))
SANAncestors = set(FindAncestors("SAN"))

common = YOUAncestors.intersection(SANAncestors) # find common ancestors
depths = []
for i in common:
  depths.append(FindDepth(orbits,i))
commondepth = max(depths) # find closest common ancestor

you = FindDepth(orbits, "YOU")
san = FindDepth(orbits, "SAN")

solution = you + san - 2* commondepth - 2 # off by two errors :)
print("Number of orbital transfers needed for part 2: ", solution)
