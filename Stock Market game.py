import random

day = [1]
hour = [1]
money = 0
ownedstock1 = [0]
ownedstock2 = [0]
ownedstock3 = [0]
ownedstock4 = [0]
ownedstock5 = [0]
ownedstock6 = [0]
ownedstock7 = [0]
ownedstock8 = [0]
stock1price = [150] #bluechip
stock2price = [30] #crypto
stock3price = [15] #medium
confidence3 = [50]
stock4price = [20] #medium
confidence4 = [50]
stock5price = [30] #medium
confidence5 = [50]
stock6price = [40] #medium
confidence6 = [50]
stock7price = [2] #penny
stock8price = [3] #penny
confidence1 = [50] #1-100 --> 1-25 = low confidence --- 25-75 = average confidence --- 75-100 = high confidence
fakevar1 = [1] #fake variable for penny stocks
goal = 2000
command = 1
game = 0

def incrementtime(a,b) :
    if a[0] != 12 :
        a[0] = a[0] + 1
    else :
        b[0] = b[0] + 1
        a[0] = a[0] + 1 #if hour is 13 run like 5 price change and then set hour to 1

def lowconpricechange(a,b) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
    elif lowconrandom >= 21 and lowconrandom <= 50 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
    elif lowconrandom >= 51 and lowconrandom <= 70 :
        a[0] = a[0]
        b[0] = b[0]
    elif lowconrandom >= 71 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2

def mediumconpricechange(a,b) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
    elif mediumconrandom >= 11 and mediumconrandom <= 35 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
    elif mediumconrandom >= 36 and mediumconrandom <= 60 :
        a[0] = a[0]
        b[0] = b[0]
    elif mediumconrandom >= 61 and mediumconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2

def highconpricechange(a,b) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
    elif highconrandom >= 26 and highconrandom <= 50 :
        a[0] = a[0]
        b[0] = b[0]
    elif highconrandom >= 51 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2

def bluechippricechange(a) :
    bluechiprandom = random.randint(1,100)
    if bluechiprandom >= 1 and bluechiprandom <= 15 :
        a[0] = float(a[0]) * .97
    elif bluechiprandom >= 16 and bluechiprandom <= 30 :
        a[0] = a[0]
    elif bluechiprandom >= 31 and bluechiprandom <= 75 :
        a[0] = float(a[0]) * 1.02
    elif bluechiprandom >= 76 and bluechiprandom <= 90 :
        a[0] = float(a[0]) * 1.05
    else :
        a[0] = float(a[0]) * 1.08
    
def cryptopricechange(a) :
    cryptorandom = random.randint(1,100)
    if cryptorandom >= 1 and cryptorandom <= 5 :
        a[0] = float(a[0]) * .5
    elif cryptorandom >= 6 and cryptorandom <= 20 :
        a[0] = float(a[0]) * .75
    elif cryptorandom >= 21 and cryptorandom <= 40 :
        a[0] = float(a[0]) * .9
    elif cryptorandom >= 41 and cryptorandom <= 60 :
        a[0] = a[0]
    elif cryptorandom >= 61 and cryptorandom <= 80 :
        a[0] = float(a[0]) * 1.10
    elif cryptorandom >= 81 and cryptorandom <= 95 :
        a[0] = float(a[0]) * 1.50
    else :
        a[0] = float(a[0]) * 2

def showprice() :
    print("Price of Glogel stock:", stock1price[0])
    print("Price of Britcoin stock:", stock2price[0])
    print("Price of Silicon Mountain stock:", stock3price[0])
    print("Price of Obelisk of the Dark Gods stock:", stock4price[0])
    print("Price of corka cola stock:", stock5price[0])
    print("Price of popsi stock:", stock6price[0])
    print("Price of Super Terrifying Haunted House Emporium stock:", stock7price[0])
    print("Price of Dolphin Rodeo Inc. stock:", stock8price[0])

def showowned() :
    print("Owned Glogel stock:", ownedstock1[0])
    print("Owned Britcoin stock:", ownedstock2[0])
    print("Owned Silicon Mountain stock:", ownedstock3[0])
    print("Owned Obelisk of the Dark Gods stock:", ownedstock4[0])
    print("Owned corka cola stock:", ownedstock5[0])
    print("Owned popsi stock:", ownedstock6[0])
    print("Owned Super Terrifying Haunted House Emporium stock:", ownedstock7[0])
    print("Owned Dolphin Rodeo Inc. stock:", ownedstock8[0])

def showwallet() :
    global money
    print("You have $" + money)

def buy() :
    global money
    pickstock = 0
    purchacestock = 0
    while pickstock == 0 :
        if 
def sell() :
    global money


def whatcommand() :
    command = 1
    command = input("what do you want to do?(buy,sell,info,end,help)")
    while command.lower() != "buy" or command.lower() != "sell" or command.lower() != "info" or command.lower() != "end" or command.lower() != "help" or command.lower() != "price" : #add more?
        if command.lower() != "buy" or command.lower() != "sell" or command.lower() != "info" or command.lower() != "end" or command.lower() != "help" or command.lower() != "price" : #if add in above line add here
            print("invalid command")
            command = input("what do you want to do?(buy,sell,price,owned,money,end,help)")
        else :
            break
    if command.lower() == "buy" :
        buy()
    elif command.lower() == "sell" :
        sell()
    elif command.lower() == "price" :
        showprice()
    elif command.lower() == "owned" :
        showowned()
    elif command.lower() == "money" :
        showwallet()
    elif command.lower() == "end" :
        incrementtime()
    else : #help command
        help()


def easymodegame() :
    print("Welcome to the easy mode of MSMG by SPDC Technologies. In order to win, you have to [FILL IN LATER]. In order to start, run the 'help' command.")
    whatcommand()
        
def mediummodegame() :
    print("test")
    whatcommand()

def hardmodegame() :
    print("test")
    whatcommand()
    
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