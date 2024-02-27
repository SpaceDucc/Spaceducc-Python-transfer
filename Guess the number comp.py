import random

number = int(input("Pick a number for the computer to guess:"))
while number > 100 or number < 1 :
  print("invalid number")
  number = int(input("Pick a number for the computer to guess:"))

guess = random.randint(1,100)

def smallorlargecomp(a,b) :
  x=1
  min = 1
  max = 100
  while a != b :
    x+=1 
    if a < b :
      print("The number is larger")
      min = a
      a = random.randint(min,max)
    elif a > b :
      print("The number is smaller")
      max = a
      a = random.randint(min,max)
  else :
    print("The computer guessed correctly")
    print("The computer guessed", x, "times")

smallorlargecomp(guess, number)