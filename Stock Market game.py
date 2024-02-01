import random

day = 1
hour = 1
money = 0
stock1price = 150 #bluechip
stock2price = 30 #crypto
stock3price = 15 #medium
stock4price = 20 #medium
stock5price = 30 #medium
stock6price = 40 #medium
stock7price = 2 #penny
stock8price = 3 #penny
confidence = 50 #1-100 --> 1-25 = low confidence --- 25-75 = average confidence --- 75-100 = high confidence
goal = 2000

game = 0

while game != 1 :
    print("Welcome to The Miniture Stock Market Game by SPDC Technologies.")
    difficulty = input("Please select a difficulty(easy, medium, or hard):")
    if difficulty.lower() == "easy" :
        money = 300
        #easy difficulty gamemode
        game = 1
    elif difficulty.lower() == "medium" :
        money = 200
        #medium difficulty gamemode
        game = 1
    elif difficulty.lower() == "hard" :
        money = 100
        #hard difficulty gamemode
        game = 1
    else :
        print("invalid difficulty")
        input("Please select a difficulty(easy, medium, or hard):")

