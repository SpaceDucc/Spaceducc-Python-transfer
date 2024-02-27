import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100:"))

def smallorlarge(a,b) :
  x=1
  while a != b :
    x+=1 
    if a < 1 :
      x-=1
      print("invalid guess")
      a = int(input("Guess a new number between 1 and 100:"))
    elif a > 100 :
      x-=1
      print("invalid guess")
      a = int(input("Guess a new number between 1 and 100:"))  
    elif a < b :
      print("The number is larger")
      a = int(input("Guess a new number between 1 and 100:"))
    elif a > b :
      print("The number is smaller")
      a = int(input("Guess a new number between 1 and 100:"))

  else :
    print("You guessed correctly")
    print("you guessed", x, "times")

smallorlarge(guess, number)
