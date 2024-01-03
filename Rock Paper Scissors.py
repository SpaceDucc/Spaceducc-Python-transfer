import random

choice = ["Rock", "Paper", "Scissors"]
numberofrounds = int(input("How many rounds would you like? Please chose an odd number of rounds:"))
playerchoice = 0
computerchoice = choice[random.randint(0,2)]


def rockpaperscissors(a,b,c) :
    maxwinorlose = int((float(c)/2) + 0.5)
    wins = 0 
    losses = 0
    rounds = 0
    a = input("Rock, Paper, or Scissors:").upper()
    while c != int(c) and (float(c) % 2) != 1:
        if c != int(c) :
            print("That is not a number")
            c = input("How many rounds would you like? Please chose an odd number of rounds:")
        elif (float(c) % 2) != 1 :
            print("That number is not odd")
            c = input("How many rounds would you like? Please chose an odd number of rounds:")
            maxwinorlose = int((float(c)/2) + 0.5)

    while rounds != c + 1:
        if a.upper() == b.upper() :
            print("You both chose", b.capitalize() + ". You tied!")
            print("Try Again!")
            b = choice[random.randint(0,2)]
            rounds = rounds + 1
        elif a.upper() == "ROCK" :
            if b.upper() == "PAPER" :
                losses = (int(losses) + 1)
                print("The Computer chose", b.capitalize() + ". You have lost", losses, "rounds.")
                b = choice[random.randint(0,2)]
                rounds = rounds + 1
            else :
                wins = (int(wins) + 1)
                print("The Computer chose", b.capitalize() + ". You have won", wins, "rounds.")
                b = choice[random.randint(0,2)]
                rounds = rounds + 1
        elif a.upper() == "PAPER" :
            if b.upper() == "SCISSORS" :
                losses = (int(losses) + 1)
                print("The Computer chose", b.capitalize() + ". You have lost", losses, "rounds.")
                b = choice[random.randint(0,2)]
                rounds = rounds + 1
            else :
                wins = (int(wins) + 1)
                print("The Computer chose", b.capitalize() + ". You have won", wins, "rounds.")
                b = choice[random.randint(0,2)]
                rounds = rounds + 1
        elif a.upper() == "SCISSORS" :
            if b.upper() == "ROCK" :
                losses = (int(losses) + 1)
                print("The Computer chose", b.capitalize() + ". You have lost", losses, "rounds.")
                b = choice[random.randint(0,2)]
                rounds = rounds + 1
            else :
                wins = (int(wins) + 1)
                print("The Computer chose", b.capitalize() + ". You have won", wins, "rounds.")
                b = choice[random.randint(0,2)]
                rounds = rounds + 1
        else :
            print("Invalid Choice")

        if losses == maxwinorlose :
            print("You have lost in", rounds, "rounds.")
            rounds = c + 1
        elif wins == maxwinorlose :
            print("You have won in", rounds, "rounds.")
            rounds = c + 1
        a = input("Rock, Paper, or Scissors:").upper()

rockpaperscissors(playerchoice, computerchoice.upper(), numberofrounds)