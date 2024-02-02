import random

day = 1
hour = 1
money = 0
stock1price = 150 #bluechip
stock2price = 30 #crypto
stock3price = 15 #medium
confidence3 = 50
stock4price = 20 #medium
confidence4 = 50
stock5price = 30 #medium
confidence5 = 50
stock6price = 40 #medium
confidence6 = 50
stock7price = 2 #penny
stock8price = 3 #penny
confidence1 = 50 #1-100 --> 1-25 = low confidence --- 25-75 = average confidence --- 75-100 = high confidence
fakevar1 = 1 #fake variable for penny stocks
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

def incrementtime(a,b) :
    if a != 12 :
        a = a + 1
    else :
        b = b + 1
        a = 1

def lowconpricechange(a,b) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a = float(a) * .9
        b = b - 2
    elif lowconrandom >= 21 and lowconrandom <= 50 :
        a = float(a) * .95
        b = b - 1
    elif lowconrandom >= 51 and lowconrandom <= 70 :
        a = a
        b = b
    elif lowconrandom >= 71 and lowconrandom <= 90 :
        a = float(a) * 1.05
        b = b + 1
    else :
        a = float(a) * 1.10
        b = b + 2

def mediumconpricechange(a,b) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a = float(a) * .9
        b = b - 2
    elif mediumconrandom >= 11 and mediumconrandom <= 35 :
        a = float(a) * .95
        b = b - 1
    elif mediumconrandom >= 36 and mediumconrandom <= 60 :
        a = a
        b = b
    elif mediumconrandom >= 61 and mediumconrandom <= 90 :
        a = float(a) * 1.05
        b = b + 1
    else :
        a = float(a) * 1.10
        b = b + 2

def highconpricechange(a,b) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a = float(a) * .9
        b = b - 2
    elif highconrandom >= 6 and highconrandom <= 25 :
        a = float(a) * .95
        b = b - 1
    elif highconrandom >= 26 and highconrandom <= 50 :
        a = a
        b = b
    elif highconrandom >= 51 and highconrandom <= 80 :
        a = float(a) * 1.05
        b = b + 1
    else :
        a = float(a) * 1.10
        b = b + 2

def bluechippricechange(a) :
    bluechiprandom = random.randint(1,100)
    if bluechiprandom >= 1 and bluechiprandom <= 15 :
        a = float(a) * .97
    elif bluechiprandom >= 16 and bluechiprandom <= 30 :
        a = a
    elif bluechiprandom >= 31 and bluechiprandom <= 75 :
        a = float(a) * 1.02
    elif bluechiprandom >= 76 and bluechiprandom <= 90 :
        a = float(a) * 1.05
    else :
        a = float(a) * 1.08
    
def cryptopricechange(a) :
    cryptorandom = random.randint(1,100)
    if cryptorandom >= 1 and cryptorandom <= 5 :
        a = float(a) * .5
    elif cryptorandom >= 6 and cryptorandom <= 20 :
        a = float(a) * .75
    elif cryptorandom >= 21 and cryptorandom <= 40 :
        a = float(a) * .9
    elif cryptorandom >= 41 and cryptorandom <= 60 :
        a = a
    elif cryptorandom >= 61 and cryptorandom <= 80 :
        a = float(a) * 1.10
    elif cryptorandom >= 81 and cryptorandom <= 95 :
        a = float(a) * 1.5
    else :
        a = float(a) * 2

def buy(a,b) : #where a is amount and b is the stock
    