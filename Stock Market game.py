import random

day = 1
hour = 1
money = 0
ownedstock1 = 0
ownedstock2 = 0
ownedstock3 = 0
ownedstock4 = 0
ownedstock5 = 0
ownedstock6 = 0
ownedstock7 = 0
ownedstock8 = 0
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
command = 1
game = 0

def incrementtime(a,b) :
    if a != 12 :
        a = a + 1
    else :
        b = b + 1
        a = a + 1 #if hour is 13 run like 5 price change and then set hour to 1

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
        a = float(a) * 1.50
    else :
        a = float(a) * 2

def showinfo() :
    print("Price of (STOCKNAME1):", stock1price)
    print("Price of (STOCKNAME2):", stock2price)
    print("Price of (STOCKNAME3):", stock3price)
    print("Price of (STOCKNAME4):", stock4price)
    print("Price of (STOCKNAME5):", stock5price)
    print("Price of (STOCKNAME6):", stock6price)
    print("Price of (STOCKNAME7):", stock7price)
    print("Price of (STOCKNAME8):", stock8price)
    print("Owned stock")

def whatcommand() :
    command = 1
    command = input("what do you want to do?(buy,sell,info,end,help)")
    while command.lower() != "buy" or command.lower() != "sell" or command.lower() != "info" or command.lower() != "end" or command.lower() != "help" : #add more?
        if command.lower() != "buy" or command.lower() != "sell" or command.lower() != "info" or command.lower() != "end" or command.lower() != "help" : #if add in above line add here
            print("invalid command")
            command = input("what do you want to do?(buy,sell,info,end,help)")
        else :
            break
    if command.lower() == "buy" :
        print("TEST")
        #replace with buy command
    elif command.lower() == "sell" :
        print("TEST")
        #replace with sell command
    elif command.lower() == "info" :
        print("TEST")
        #replace with info command
    elif command.lower() == "end" :
        print("TEST")
        #replace with end hour command
    else : #help command
        print("TEST")
        #replace with help command


def easymodegame() :
    print("Welcome to the easy mode of MSMG by SPDC Technologies. In order to win, you have to [FILL IN LATER]. In order to start, run the 'help' command.")
        
def mediummodegame() :
    print("tet")

def hardmodegame() :
    print("tet")
    
def startgame() :
    global money
    global game
    while game != 1 :
        print("Welcome to The Miniture Stock Market Game by SPDC Technologies.")
        difficulty = input("Please select a difficulty(easy, medium, or hard):")
        if difficulty.lower() == "easy" :
            money = 300
            easymodegame()
            game = 1
        elif difficulty.lower() == "medium" :
            money = 200
            mediummodegame()
            game = 1
        elif difficulty.lower() == "hard" :
            money = 100
            hardmodegame()
            game = 1
        else :
            print("invalid difficulty")
            input("Please select a difficulty(easy, medium, or hard):")

startgame()