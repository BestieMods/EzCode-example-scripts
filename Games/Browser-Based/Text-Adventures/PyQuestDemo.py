import sys
print("Initialized PYQUEST Alpha 0.0.1")
print("Welcome to PyQuest! There are 3 simple trials you can choose through")
start-pyquest = input("Show trials? Y/N")
if start-pyquest == "Y":
  print("Ok, the trials are: Math, Dungeon, and Decipher")
elif start-pyquest == "N":
  sys.exit("I guess you are not ready, come back when you are!")
else:
  sys.exit("Error code 1: invalid input. Try doing Y or N if you can!")

choice-trial = input("Choose the trial you would like to do! Math/Dungeon/Decipher")

if choice-trial == "Math":
  correct = 0
  print("Welcome to the Math trial!")
  print("if all 3 are correct, you pass!")
  question-one = input("Let's start easy: What is 152 + 238?")
  if question-one == "390":
    print("Correct!")
    correct += 1
  else:
    print("Incorrect!")
  question-two = input("Let's ramp it up: What is 152 * 238 + 3832?")
  if question-two == "40008":
    print("Correct!")
    correct += 1
  else:
    print("Incorrect!")
  print("Oh god")
  print("Oh no")
  print("time for the hardest on of your existence!")
  question-three = input("Good luck: What is 1 + 1?")
  if question-three == "2"
    print("Theres no way. You did it.")
    print("CORRRECT!!!")
    correct += 1
  print("Nice job!")
  print("Let's see the score: ")
  if correct == 3:
    print("You won! nice :P")
    print("You got 3/3!")
  else:
    print("That was close! you mustv'e gotten 2/3 or less")
    print("It was probably the last one, that one was hard :(")
    print("good job tho :P")
# will add the other 2 :P
    
