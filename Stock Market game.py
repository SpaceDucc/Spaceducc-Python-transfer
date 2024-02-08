import random

day = [1]
hour = [1]
moneygoal = 2000
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
#1-100 --> 1-25 = low confidence --- 25-75 = average confidence --- 75-100 = high confidence
fakevar1 = [1] #fake variable for penny stocks
goal = 2000
command = 1
game = 0




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
    print("Owned corka Cola stock:", ownedstock5[0])
    print("Owned Popsi stock:", ownedstock6[0])
    print("Owned Super Terrifying Haunted House Emporium stock:", ownedstock7[0])
    print("Owned Dolphin Rodeo Inc. stock:", ownedstock8[0])

def showwallet() :
    global money
    print("You have $" + money)

def stockhelp() :
    print("You want to buy and sell stock at the correct times in order to make the most money. You do this using the different commands.")
    print("'buy' allows you to buy stocks, and 'sell' allows you to sell the your stocks.")
    print("'price' lets you see the prices of the stocks, 'owned' lets you see how much of each stock you own, 'money' lets you see how much money you have.")
    print("'end' will end the hour you are on and change the prices of the stocks, and on hour 12, the day will roll over and prices will change more signifigantly, you can see the time with the 'time' command.")
    print("")

def buy() :
    global money
    mathmoney = 0
    pickstock = 0
    purchacestock = 0
    whatstock = 0
    howmuch = 0
    while pickstock == 0 :
        whatstock = input("What Stock Do you want to buy?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
        if whatstock.lower() == "glogel" or whatstock.lower() == "britcoin" or whatstock.lower() == "silicon" or whatstock.lower() == "obelisk" or whatstock.lower() == "corka cola" or whatstock.lower() == "popsi" or whatstock.lower() == "haunted house" or whatstock.lower() == "dolphin" :
            pickstock = 1
        else :
            print("That is not a stock")
            whatstock = input("What Stock Do you want to buy?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
    while purchacestock == 0 :
        if whatstock.lower() == "glogel" :
            howmuch = input("how many Glogel stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Glogel stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock1price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock1[0] = ownedstock1[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "britcoin" :
            howmuch = input("how many Britcoin stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Britcoin stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock2price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock2[0] = ownedstock2[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "silicon" :
            howmuch = input("how many Silicon Mountain stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Silicon Mountain stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock3price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock3[0] = ownedstock3[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "obelisk" :
            howmuch = input("how many Obelisk of the Dark Gods stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Obelisk of the Dark Gods stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock4price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock4[0] = ownedstock4[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "corka cola" :
            howmuch = input("how many Corka Cola stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Corka Cola stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock5price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock5[0] = ownedstock5[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "popsi" :
            howmuch = input("how many Popsi stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Popsi stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock6price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock6[0] = ownedstock6[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "haunted house" :
            howmuch = input("how many Super Terrifying Haunted House Emporium stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Super Terrifying Haunted House Emporium stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock7price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock7[0] = ownedstock7[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "dolphin" :
            howmuch = input("how many Dolphin Rodeo Inc. stock do you want to buy:")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Dolphin Rodeo Inc. stock do you want to buy:")
                else :
                    continue
            mathmoney = int(stock8price[0]) * howmuch
            if mathmoney > money :
                print("You do not have enough money")
            else :
                ownedstock8[0] = ownedstock8[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        else :
            print("[THIS SHOULDN'T HAPPEN]")

def sell() :
    global money
    mathmoney = 0
    pickstock = 0
    sellstock = 0
    whatstock = 0
    howmuch = 0
    while pickstock == 0 :
        whatstock = input("What Stock Do you want to sell?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
        if whatstock.lower() == "glogel" or whatstock.lower() == "britcoin" or whatstock.lower() == "silicon" or whatstock.lower() == "obelisk" or whatstock.lower() == "corka cola" or whatstock.lower() == "popsi" or whatstock.lower() == "haunted house" or whatstock.lower() == "dolphin" :
            pickstock = 1
        else :
            print("That is not a stock")
            whatstock = input("What Stock Do you want to sell?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
    
    while sellstock == 0 :
        if whatstock.lower() == "glogel" :
            howmuch = input("how many Glogel stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Glogel stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock1price[0]) * howmuch
            if ownedstock1[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock1[0] = ownedstock1[0] - howmuch
                money = money + mathmoney
                sellstock = 1

        if whatstock.lower() == "britcoin" :
            howmuch = input("how many Britcoin stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Britcoin stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock2price[0]) * howmuch
            if ownedstock2[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock2[0] = ownedstock2[0] - howmuch
                money = money + mathmoney
                sellstock = 1
        
        if whatstock.lower() == "silicon" :
            howmuch = input("how many Silicon Mountain stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Silicon Mountain stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock3price[0]) * howmuch
            if ownedstock3[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock3[0] = ownedstock3[0] - howmuch
                money = money + mathmoney
                sellstock = 1

        if whatstock.lower() == "obelisk" :
            howmuch = input("how many Obelisk of the Dark Gods stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Obelisk of the Dark Gods stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock4price[0]) * howmuch
            if ownedstock4[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock4[0] = ownedstock4[0] - howmuch
                money = money + mathmoney
                sellstock = 1

        if whatstock.lower() == "corka cola" :
            howmuch = input("how many Corka Cola stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Corka Cola stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock5price[0]) * howmuch
            if ownedstock5[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock5[0] = ownedstock5[0] - howmuch
                money = money + mathmoney
                sellstock = 1

        if whatstock.lower() == "popsi" :
            howmuch = input("how many Popsi stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Popsi stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock6price[0]) * howmuch
            if ownedstock6[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock6[0] = ownedstock6[0] - howmuch
                money = money + mathmoney
                sellstock = 1

        if whatstock.lower() == "haunted house" :
            howmuch = input("how many Super Terrifying Haunted House Emporium stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Super Terrifying Haunted House Emporium stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock7price[0]) * howmuch
            if ownedstock7[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock7[0] = ownedstock7[0] - howmuch
                money = money + mathmoney
                sellstock = 1

        if whatstock.lower() == "dolphin" :
            howmuch = input("how many Dolphin Rodeo Inc. stock do you want to sell?")
            while howmuch != int(howmuch) :
                if howmuch != int(howmuch) :
                    print("that is not a number")
                    howmuch = input("how many Dolphin Rodeo Inc. stock do you want to sell:")
                else :
                    continue
            mathmoney = int(stock8price[0]) * howmuch
            if ownedstock8[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock8[0] = ownedstock8[0] - howmuch
                money = money + mathmoney
                sellstock = 1


def incrementtime() :
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price[0])
        cryptopricechange(stock2price[0])
        mediumconpricechange(stock7price[0], fakevar1)
        mediumconpricechange(stock8price[0], fakevar1)

        if confidence3[0] < 25 :
            lowconpricechange(stock3price[0], confidence3[0])
        elif confidence3[0] > 75 :
            highconpricechange(stock3price[0], confidence3[0])
        else :
            mediumconpricechange(stock3price[0], confidence3[0])

        if confidence4[0] < 25 :
            lowconpricechange(stock4price[0], confidence4[0])
        elif confidence4[0] > 75 :
            highconpricechange(stock4price[0], confidence4[0])
        else :
            mediumconpricechange(stock4price[0], confidence4[0])

        if confidence5[0] < 25 :
            lowconpricechange(stock5price[0], confidence5[0])
        elif confidence5[0] > 75 :
            highconpricechange(stock5price[0], confidence5[0])
        else :
            mediumconpricechange(stock5price[0], confidence5[0])

        if confidence6[0] < 25 :
            lowconpricechange(stock6price[0], confidence6[0])
        elif confidence6[0] > 75 :
            highconpricechange(stock6price[0], confidence6[0])
        else :
            mediumconpricechange(stock6price[0], confidence6[0])

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        while fakevar2 != 5 :
            bluechippricechange(stock1price[0])
        cryptopricechange(stock2price[0])
        mediumconpricechange(stock7price[0], fakevar1)
        mediumconpricechange(stock8price[0], fakevar1)

        if confidence3[0] < 25 :
            lowconpricechange(stock3price[0], confidence3[0])
        elif confidence3[0] > 75 :
            highconpricechange(stock3price[0], confidence3[0])
        else :
            mediumconpricechange(stock3price[0], confidence3[0])

        if confidence4[0] < 25 :
            lowconpricechange(stock4price[0], confidence4[0])
        elif confidence4[0] > 75 :
            highconpricechange(stock4price[0], confidence4[0])
        else :
            mediumconpricechange(stock4price[0], confidence4[0])

        if confidence5[0] < 25 :
            lowconpricechange(stock5price[0], confidence5[0])
        elif confidence5[0] > 75 :
            highconpricechange(stock5price[0], confidence5[0])
        else :
            mediumconpricechange(stock5price[0], confidence5[0])

        if confidence6[0] < 25 :
            lowconpricechange(stock6price[0], confidence6[0])
        elif confidence6[0] > 75 :
            highconpricechange(stock6price[0], confidence6[0])
        else :
            mediumconpricechange(stock6price[0], confidence6[0])

        fakevar2 = fakevar2 + 1
        hour[0] = 1

def whattime() :
    print("day", day[0] + ", hour", hour[0])

def whatcommand() :
    command = 1
    command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
    print(command)
    while command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #add more?
        if command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #if add in above line add here
            print("invalid command")
            command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
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
    elif command.lower() == "time" :
        whattime()
    else : #help command
        stockhelp()


def easymodegame() :
    print("Welcome to the easy difficulty mode of MSMG by SPDC Technologies. In order to win, you have to [FILL IN LATER]. In order to start, run the 'help' command.")
    whatcommand()

def mediummodegame() :
    global moneygoal
    print("Welcome to the medium difficulty mode of MSMG by SPDC Technologies. In order to win, you have to [FILL IN LATER]. In order to start, run the 'help' command")
    while goal == 0:
        if money < moneygoal :
            whatcommand()
        else :
            print("you win")
            game = 0


def hardmodegame() :
    print("test")
    whatcommand()
    
def startgame() :
    global money
    global game
    global goal
    goal = 0
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