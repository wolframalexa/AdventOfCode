f = open('day3input.txt', "r")
lines = f.readlines()
firstwire = map(str, lines[0].split(','))
secondwire = map(str, lines[1].split(','))

x1 = []
y1 = []
x2 = []
y2 = []
intersectionX = []
intersectionY = []
ManhattanDistances = []

def followCommand(xArray, yArray, instructions):
  xpos = 0
  ypos = 0

  for i in instructions:
    direction = i[0]
    length = int(i[1:])
    if direction == "R":
      xpos = xpos + length
      xArray.append(xpos)
      yArray.append(ypos)
    elif direction == "L":
      xpos = xpos - length
      xArray.append(xpos)
      yArray.append(ypos)
    elif direction == "U":
      ypos = ypos + length
      yArray.append(ypos)
      xArray.append(xpos)
    elif direction == "D":
      ypos = ypos - length
      yArray.append(ypos)
      xArray.append(xpos)

def findLower(x1,x2):
  if x1 < x2:
    return x1
  else:
    return x2

def findHigher(x1,x2):
  if x1 > x2:
    return x1
  else:
    return x2

def findIntersections(xArray1,yArray1,xArray2,yArray2):
  loop = len(xArray1)-1
  for i in range(0,loop): # all arrays should be of same size
    # assuming no lines are superposed, only vertical lines can cross horizontal lines
    for j in range(0,loop):
      x1_lower = findLower(xArray1[i],xArray1[i+1])
      y1_lower = findLower(yArray1[i],yArray1[i+1])
      x1_higher = findHigher(xArray1[i],xArray1[i+1])
      y1_higher = findHigher(yArray1[i],yArray1[i+1])

      if xArray1[i] == xArray1[i+1] and yArray2[j] == yArray2[j+1] and y1_lower < yArray2[j] and yArray2[j] < y1_higher and x1_lower < xArray2[j] and xArray2[j] < x1_higher:
        print "if statement"
        intersectionX.append(xArray1[i])
        intersectionY.append(yArray2[j])
      elif yArray1[i] == yArray1[i+1] and xArray2[j] == xArray2[j+1] and x1_lower < xArray2[j] and xArray2[j] < x1_higher and y1_lower < yArray2[j] and yArray2[j] < y1_higher:
	print "elif statement"
        intersectionX.append(xArray2[j])
        intersectionY.append(yArray1[i])
# lines are vertical and horizontal: so they intersect when the x of the vertical line is in between the x of the points of the horizontal line. the opposite must also be true


def findManhattanDistance(xArray,yArray):
  for i in range(0,len(xArray)):
    x = abs(xArray[i])+abs(yArray[i])
    ManhattanDistances.append(x)

followCommand(x1,y1,firstwire)
followCommand(x2,y2,secondwire)

findIntersections(x1,y1,x2,y2)
print intersectionX
print intersectionY
findManhattanDistance(intersectionX,intersectionY)
# minDistance = min(ManhattanDistances)

# print "The minimal distance is: ",minDistance
