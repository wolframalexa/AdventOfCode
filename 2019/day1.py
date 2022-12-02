# Problem statement: determine the amount of fuel needed to get Santa's sleigh off the ground, using the rocket equation

import math

f = open('day1input.txt', "r")
numbers = f.readlines()
fuelTotal = 0

# Find fuel necessary according to rocket equation
def FindFuel(number):
  Fuel = math.floor(number/3)-2
  return Fuel;

# Part 1: Fuel for cargo only
for line in numbers:
  partFuel = FindFuel(int(line))
  fuelTotal = fuelTotal + partFuel
print 'The total fuel for part 1 is: ',fuelTotal


# Part 2: You need fuel to transport the fuel!
fuelTotal = 0

for line in numbers:
  loadRemaining = int(line)
  while loadRemaining > 0:
    loadRemaining = FindFuel(loadRemaining)
    if loadRemaining > 0: # don't add negative fuel values
      fuelTotal = fuelTotal + loadRemaining

print 'The total fuel for part 2 is: ',fuelTotal

f.close()
