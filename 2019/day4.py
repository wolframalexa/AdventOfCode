def increases(number):
  number = list(str(number))
  if number == sorted(number):
    return True
  return False

def hasDouble(number):
  number = list(str(number))
  for i in range(5):
    if number[i] == number[i+1] and (i == 0 or number[i]!=number[i-1]) and (i == 4 or number[i] != number[i+2]):
      return True
  return False

def findPassword1(number):
  number = str(number)
  repeated = 0

  for i in range(0, len(number)-1):
    if increases(number) and number[i] == number [i+1]:
      repeated = repeated + 1
  return repeated

def isPassword2(number):
  if increases(number) and hasDouble(number):
    return True

def isPassword1(number):
  repeated = findPassword1(number)
  if repeated != 0:
    return True

# Part 1
possiblePasswords = []

for i in range(172851,675869):
  if isPassword1(i) == True:
    possiblePasswords.append(i)
numPassword = len(possiblePasswords)

print "Number of possible passwords for part 1:",numPassword


# Part 2
possiblePasswords2 = []

for i in range(172851,675869):
  if isPassword2(i) == True:
    possiblePasswords2.append(i)
numPassword = len(possiblePasswords2)

print "Number of possible passwords for part 2:",numPassword

