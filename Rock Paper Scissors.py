import random

choice = ["Rock", "Paper", "Scissors"]
playerchoice = input("Rock, Paper, or Scissors:")
computerchoice = choice[random.randint(0,2)]
#if remainder = 0 get new number if remainder exists add +0.5
def rockpaperscissors(a,b) :
    game = 0
    while game == 0 :
        if a == b :
            print("You both chose", b.capitalize() + ". You tied!")
            print("Try Again!")
            a = input("Rock, Paper, or Scissors:").upper()
        elif a == "ROCK" :
            if b == "PAPER" :
                print("The Computer chose", b.capitalize() + ". You lose!")
                game = 1
            else :
                print("The Computer chose", b.capitalize() + ". You win!")
                game = 1
        elif a == "PAPER" :
            if b == "SCISSORS" :
                print("The Computer chose", b.capitalize() + ". You lose!")
                game = 1
            else :
                print("The Computer chose", b.capitalize() + ". You win!")
                game = 1
        elif a == "SCISSORS" :
            if b == "ROCK" :
                print("The Computer chose", b.capitalize() + ". You lose!")
                game = 1
            else :
                print("The Computer chose", b.capitalize() + ". You win!")
                game = 1
        else :
            print("Invalid Choice")
            a = input("Rock, Paper, or Scissors:").upper()

rockpaperscissors(playerchoice.upper(), computerchoice.upper())