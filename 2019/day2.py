f = open('day2input.txt', "r")
lines = f.readlines()
numbers = map(int, lines[0].split(','))


# Part 1: Figure out the code at 0
i = 0
while i < len(numbers):
  if numbers[i] == 1:
    numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
  elif numbers[i] == 2:
    numbers[numbers[i+3]] = numbers[numbers[i+1]]*numbers[numbers[i+2]]
  elif numbers[i] == 99:
    print "Part 1 answer: ",numbers[0]
    break
  i = i + 4

# Part 2: Find inputs that produce the output 19690720
for noun in range(100):
  for verb in range(100):
    numbers =  map(int, lines[0].split(',')) # reset numbers to the input at every loop
    numbers[1] = noun
    numbers[2] = verb

    i = 0
    while i < len(numbers):
      opcode = numbers[i]
      if opcode == 1:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
      elif opcode == 2:
        numbers[numbers[i+3]] = numbers[numbers[i+1]]*numbers[numbers[i+2]]
      else:
        break
      i = i + 4
    if numbers[0] == 19690720:
      print "Noun: ",noun
      print "Verb: ",verb
      answer = 100*noun+verb
      print "The answer for part 2 is: ",answer
      break
f.close()
