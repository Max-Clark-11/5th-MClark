#ImportRandom
import random

Number = int(input("Type any whole number:"))
print(Number)
#Variables
Guess = 0
Answer = random.randint(1, Number)
Message = int(input("Guess a number between 1 and " + str(Number) + ":"))
Correct = False
#Game
while Correct == False:
    if Message == Answer:
        Message = ("You Win!")
        print(Message)
        Correct = True
    else:
         if Message >= Answer:
             print("lower")
             Guess = Guess + 1
             print("Number of guesses:" + str(Guess))
             Message = int(input("Guess a number between 1 and " + str(Number) + ":"))
         else:
             print("higher")
             Guess = Guess + 1
             print("Number of guesses:" + str(Guess))
             Message = int(input("Guess a number between 1 and " + str(Number) + ":"))