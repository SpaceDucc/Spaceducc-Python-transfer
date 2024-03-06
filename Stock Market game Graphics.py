import random
from graphics import *

day = [1]
hour = [1]
moneygoal = 2000
money = float(0)
ownedstock1 = [0]
price1change = ["="]
ownedstock2 = [0]
price2change = ["="]
ownedstock3 = [0]
price3change = ["="]
ownedstock4 = [0]
price4change = ["="]
ownedstock5 = [0]
price5change = ["="]
ownedstock6 = [0]
price6change = ["="]
ownedstock7 = [0]
price7change = ["="]
ownedstock8 = [0]
price8change = ["="]
stock1price = [150.0] #bluechip
stock2price = [30.0] #crypto
stock3price = [15.0] #medium
confidence3 = [50]
stock4price = [20.0] #medium
confidence4 = [50]
stock5price = [30.0] #medium
confidence5 = [50]
stock6price = [40.0] #medium
confidence6 = [50]
stock7price = [2.0] #penny
stock8price = [3.0] #penny
#1-100 --> 1-25 = low confidence --- 25-75 = average confidence --- 75-100 = high confidence
fakevar1 = [1] #fake variable for penny stocks
goal = 2000
command = 1
game = 0
win1 = GraphWin("MSMG", 1200, 700)

buypt1 = Point(50,50)
buypt2 = Point(250,150)
buyrec = Rectangle(buypt1,buypt2)

buypt3 = Point(150,100)
buytext = Text(buypt3, "Buy Stock")

sellpt1 = Point(50,200)
sellpt2 = Point(250,300)
sellrec = Rectangle(sellpt1,sellpt2)

sellpt3 = Point(150,250)
selltext = Text(sellpt3, "Sell Stock")
selltext.setTextColor(color_rgb(255,255,255))

statuspt1 = Point(50,350)
statuspt2 = Point(250,450)
statusrec = Rectangle(statuspt1,statuspt2)

statuspt3 = Point(150,400)
statustext = Text(statuspt3, "Information")

timept1 = Point(50,500)
timept2 = Point(250,600)
timerec = Rectangle(timept1,timept2)

timept3 = Point(150,550)
timetext = Text(timept3, "Next Hour")

clockpt1 = Point(1000,25)
clockpt2 = Point(1100,75)
clockrec = Rectangle(clockpt1,clockpt2)

clockpt3 = Point(1050,50)
clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0])]
clocktext = Text(clockpt3, clocktexttext)

moneypt1 = Point(1000,100)
moneypt2 = Point(1100,150)
moneyrec = Rectangle(moneypt1,moneypt2)

moneypt3 = Point(1050,125)
moneytexttext = ["$",str(money)]
moneytext = Text(moneypt3, moneytexttext)

stock1pt1 = Point(120,200)
stock1pt2 = Point(320,350)
stock1rec = Rectangle(stock1pt1,stock1pt2)

stock1pt3 = Point(220,275)
stock1text = Text(stock1pt3,"Glogel Stock")

stock2pt1 = Point(360,200)
stock2pt2 = Point(560,350)
stock2rec = Rectangle(stock2pt1,stock2pt2)

stock2pt3 = Point(460,275)
stock2text = Text(stock2pt3,"Britcoin Stock")

stock3pt1 = Point(620,200)
stock3pt2 = Point(820,350)
stock3rec = Rectangle(stock3pt1,stock3pt2)

stock3pt3 = Point(720,275)
stock3text = Text(stock3pt3,"Silicon Mountain Stock")

stock4pt1 = Point(880,200)
stock4pt2 = Point(1080,350)
stock4rec = Rectangle(stock4pt1,stock4pt2)

stock4pt3 = Point(980,275)
stock4text = Text(stock4pt3,"Obelisk of the Dark Gods Stock")

stock5pt1 = Point(120,450)
stock5pt2 = Point(320,600)
stock5rec = Rectangle(stock5pt1,stock5pt2)

stock5pt3 = Point(220,525)
stock5text = Text(stock5pt3,"Corka Cola Stock")

stock6pt1 = Point(360,450)
stock6pt2 = Point(560,600)
stock6rec = Rectangle(stock6pt1,stock6pt2)

stock6pt3 = Point(460,525)
stock6text = Text(stock6pt3,"Popsi Stock")

stock7pt1 = Point(620,450)
stock7pt2 = Point(820,600)
stock7rec = Rectangle(stock7pt1,stock7pt2)

stock7pt3 = Point(720,525)
stock7text = Text(stock7pt3,"Super Terrifying Haunted House Emporium Stock")

stock8pt1 = Point(880,450)
stock8pt2 = Point(1080,600)
stock8rec = Rectangle(stock8pt1,stock8pt2)

stock8pt3 = Point(980,525)
stock8text = Text(stock8pt3,"Dolphin Rodeo Inc. Stock")

def lowconpricechange(a,b,c) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
        c[0] = "-"
    elif lowconrandom >= 21 and lowconrandom <= 45 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
        c[0] = "-"
    elif lowconrandom >= 46 and lowconrandom <= 67 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif lowconrandom >= 68 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2
        c[0] = "+"

def mediumconpricechange(a,b,c) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
        c[0] = "-"
    elif mediumconrandom >= 11 and mediumconrandom <= 30 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
        c[0] = "-"
    elif mediumconrandom >= 31 and mediumconrandom <= 55 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif mediumconrandom >= 56 and mediumconrandom <= 85 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2
        c[0] = "+"

def highconpricechange(a,b,c) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
        c[0] = "-"
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
        c[0] = "-"
    elif highconrandom >= 26 and highconrandom <= 45 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif highconrandom >= 46 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2
        c[0] = "+"

def easylowconpricechange(a,b,c) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 1
        c[0] = "-"
    elif lowconrandom >= 21 and lowconrandom <= 45 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - .5
        c[0] = "-"
    elif lowconrandom >= 46 and lowconrandom <= 67 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif lowconrandom >= 68 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1.5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 3
        c[0] = "+"

def easymediumconpricechange(a,b,c) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 1
        c[0] = "-"
    elif mediumconrandom >= 11 and mediumconrandom <= 30 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - .5
        c[0] = "-"
    elif mediumconrandom >= 31 and mediumconrandom <= 55 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif mediumconrandom >= 56 and mediumconrandom <= 85 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1.5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 3
        c[0] = "+"

def easyhighconpricechange(a,b,c) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 1
        c[0] = "-"
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - .5
        c[0] = "-"
    elif highconrandom >= 26 and highconrandom <= 45 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif highconrandom >= 46 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1.5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 3
        c[0] = "+"

def hardlowconpricechange(a,b,c) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 3
        c[0] = "-"
    elif lowconrandom >= 21 and lowconrandom <= 45 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1.5
        c[0] = "-"
    elif lowconrandom >= 46 and lowconrandom <= 67 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif lowconrandom >= 68 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + .5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 1
        c[0] = "+"

def hardmediumconpricechange(a,b,c) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 3
        c[0] = "-"
    elif mediumconrandom >= 11 and mediumconrandom <= 30 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1.5
        c[0] = "-"
    elif mediumconrandom >= 31 and mediumconrandom <= 55 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif mediumconrandom >= 56 and mediumconrandom <= 85 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + .5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 1
        c[0] = "+"

def hardhighconpricechange(a,b,c) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 3
        c[0] = "-"
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1.5
        c[0] = "-"
    elif highconrandom >= 26 and highconrandom <= 45 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif highconrandom >= 46 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + .5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 1
        c[0] = "+"

def bluechippricechange(a,c) :
    bluechiprandom = random.randint(1,100)
    if bluechiprandom >= 1 and bluechiprandom <= 10 :
        a[0] = float(a[0]) * .97
        c[0] = "-"
    elif bluechiprandom >= 11 and bluechiprandom <= 25 :
        a[0] = a[0]
        c[0] = "="
    elif bluechiprandom >= 26 and bluechiprandom <= 65 :
        a[0] = float(a[0]) * 1.02
        c[0] = "+"
    elif bluechiprandom >= 66 and bluechiprandom <= 85 :
        a[0] = float(a[0]) * 1.05
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.08
        c[0] = "+"
    
def cryptopricechange(a,c) :
    cryptorandom = random.randint(1,100)
    if cryptorandom >= 1 and cryptorandom <= 5 :
        a[0] = float(a[0]) * .5
        c[0] = "-"
    elif cryptorandom >= 6 and cryptorandom <= 20 :
        a[0] = float(a[0]) * .75
        c[0] = "-"
    elif cryptorandom >= 21 and cryptorandom <= 40 :
        a[0] = float(a[0]) * .9
        c[0] = "-"
    elif cryptorandom >= 41 and cryptorandom <= 60 :
        a[0] = a[0]
        c[0] = "="
    elif cryptorandom >= 61 and cryptorandom <= 80 :
        a[0] = float(a[0]) * 1.10
        c[0] = "+"
    elif cryptorandom >= 81 and cryptorandom <= 95 :
        a[0] = float(a[0]) * 1.50
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 2
        c[0] = "+"

def showinfo() :
    stock1priceround = str(round(stock1price[0],2))
    stock1pricelen = len(stock1priceround.split(".")[1])
    if stock1pricelen == 1 :
        print("Price of Glogel stock: $" + str(round(stock1price[0],2)) + "0", price1change[0])
    elif stock1pricelen == 2 :
        print("Price of Glogel stock: $" + str(round(stock1price[0],2)), price1change[0])
    else :
        print("error")

    stock2priceround = str(round(stock2price[0],2))
    stock2pricelen = len(stock2priceround.split(".")[1])
    if stock2pricelen == 1 :
        print("Price of Britcoin stock: $" + str(round(stock2price[0],2)) + "0", price2change[0])
    elif stock2pricelen == 2 :
        print("Price of Britcoin stock: $" + str(round(stock2price[0],2)), price2change[0])
    else :
        print("error")
    
    stock3priceround = str(round(stock3price[0],2))
    stock3pricelen = len(stock3priceround.split(".")[1])
    if stock3pricelen == 1 :
        print("Price of Silicon Mountain stock: $" + str(round(stock3price[0],2)) + "0", price3change[0])
    elif stock3pricelen == 2 :
        print("Price of Silicon Mountain stock: $" + str(round(stock3price[0],2)), price3change[0])
    else :
        print("error")
    
    stock4priceround = str(round(stock4price[0],2))
    stock4pricelen = len(stock4priceround.split(".")[1])
    if stock4pricelen == 1 :
        print("Price of Obelisk of the Dark Gods stock: $" + str(round(stock4price[0],2)) + "0", price4change[0])
    elif stock4pricelen == 2 :
        print("Price of Obelisk of the Dark Gods stock: $" + str(round(stock4price[0],2)), price4change[0])
    else :
        print("error")
    
    stock5priceround = str(round(stock5price[0],2))
    stock5pricelen = len(stock5priceround.split(".")[1])
    if stock5pricelen == 1 :
        print("Price of Corka Cola stock: $" + str(round(stock5price[0],2)) + "0", price5change[0])
    elif stock5pricelen == 2 :
        print("Price of Corka Cola stock: $" + str(round(stock5price[0],2)), price5change[0])
    else :
        print("error")

    stock6priceround = str(round(stock6price[0],2))
    stock6pricelen = len(stock6priceround.split(".")[1])
    if stock6pricelen == 1 :
        print("Price of Popsi stock: $" + str(round(stock6price[0],2)) + "0", price6change[0])
    elif stock6pricelen == 2 :
        print("Price of Popsi stock: $" + str(round(stock6price[0],2)), price6change[0])
    else :
        print("error")
    
    stock7priceround = str(round(stock7price[0],2))
    stock7pricelen = len(stock7priceround.split(".")[1])
    if stock7pricelen == 1 :
        print("Price of Super Terrifying Haunted House Emporium stock: $" + str(round(stock7price[0],2)) + "0", price7change[0])
    elif stock7pricelen == 2 :
        print("Price of Super Terrifying Haunted House Emporium stock: $" + str(round(stock7price[0],2)), price7change[0])
    else :
        print("error")
    
    stock8priceround = str(round(stock8price[0],2))
    stock8pricelen = len(stock8priceround.split(".")[1])
    if stock8pricelen == 1 :
        print("Price of Dolphin Rodeo Inc. stock: $" + str(round(stock8price[0],2)) + "0", price8change[0])
    elif stock8pricelen == 2 :
        print("Price of Dolphin Rodeo Inc. stock: $" + str(round(stock8price[0],2)), price8change[0])
    else :
        print("error")


def buy() :
    global money
    mathmoney = 0
    pickstock = 0
    purchacestock = 0
    whatstock = 0
    howmuch = 0
    fakevar3 = 0
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global clockrec
    global clocktext
    global clocktexttext
    global moneyrec
    global moneytext
    global moneytexttext
    global win1
    global stock1rec
    global stock1text
    global stock2rec
    global stock2text
    global stock3rec
    global stock3text
    global stock4rec
    global stock4text
    global stock5rec
    global stock5text
    global stock6rec
    global stock6text
    global stock7rec
    global stock7text
    global stock8rec
    global stock8text

    stock1rec.setFill(color_rgb(0,0,0))
    stock1rec.draw(win1)

    stock1text.setTextColor(color_rgb(255,255,255))
    stock1text.setSize(24)
    stock1text.draw(win1)
    
    stock2rec.setFill(color_rgb(0,0,0))
    stock2rec.draw(win1)
    
    stock2text.setTextColor(color_rgb(255,255,255))
    stock2text.setSize(24)
    stock2text.draw(win1)

    stock3rec.setFill(color_rgb(0,0,0))
    stock3rec.draw(win1)

    stock3text.setTextColor(color_rgb(255,255,255))
    stock3text.setSize(24)
    stock3text.draw(win1)

    stock4rec.setFill(color_rgb(0,0,0))
    stock4rec.draw(win1)

    stock4text.setTextColor(color_rgb(255,255,255))
    stock4text.setSize(24)
    stock4text.draw(win1)

    stock5rec.setFill(color_rgb(0,0,0))
    stock5rec.draw(win1)

    stock5text.setTextColor(color_rgb(255,255,255))
    stock5text.setSize(24)
    stock5text.draw(win1)

    stock6rec.setFill(color_rgb(0,0,0))
    stock6rec.draw(win1)

    stock6text.setTextColor(color_rgb(255,255,255))
    stock6text.setSize(24)
    stock6text.draw(win1)

    stock7rec.setFill(color_rgb(0,0,0))
    stock7rec.draw(win1)

    stock7text.setTextColor(color_rgb(255,255,255))
    stock7text.setSize(24)
    stock7text.draw(win1)

    stock8rec.setFill(color_rgb(0,0,0))
    stock8rec.draw(win1)

    stock8text.setTextColor(color_rgb(255,255,255))
    stock8text.setSize(24)
    stock8text.draw(win1)

    pickstock = 0
    whatstock = 0

    while pickstock == 0 :
        break

    while purchacestock == 0 :
        if whatstock.lower() == "glogel" :
            howmuch = int(input("how many Glogel stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid number")
                    howmuch = int(input("how many Glogel stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Glogel stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock1price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock1[0] = ownedstock1[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "britcoin" :
            howmuch = int(input("how many Britcoin stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Britcoin stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Britcoin stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock2price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock2[0] = ownedstock2[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "silicon" :
            howmuch = int(input("how many Silicon Mountain stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Silicon Mountain stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Silicon Mountain stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock3price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock3[0] = ownedstock3[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "obelisk" :
            howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock4price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock4[0] = ownedstock4[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "corka cola" :
            howmuch = int(input("how many Corka Cola stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Corka Cola stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Corka Cola stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock5price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock5[0] = ownedstock5[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "popsi" :
            howmuch = int(input("how many Popsi stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Popsi stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Popsi stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock6price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock6[0] = ownedstock6[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "haunted house" :
            howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock7price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock7[0] = ownedstock7[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "dolphin" :
            howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock8price[0]) * howmuch
            if float(mathmoney) > money :
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
    fakevar3 = 0
    while pickstock == 0 :
        whatstock = input("What Stock Do you want to sell?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
        if whatstock.lower() == "glogel" or whatstock.lower() == "britcoin" or whatstock.lower() == "silicon" or whatstock.lower() == "obelisk" or whatstock.lower() == "corka cola" or whatstock.lower() == "popsi" or whatstock.lower() == "haunted house" or whatstock.lower() == "dolphin" :
            pickstock = 1
        else :
            print("That is not a stock")
    
    while sellstock == 0 :
        if whatstock.lower() == "glogel" :
            howmuch = int(input("how many Glogel stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Glogel stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Glogel stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock1price[0]) * howmuch
            if ownedstock1[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock1[0] = ownedstock1[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "britcoin" :
            howmuch = int(input("how many Britcoin stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Britcoin stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Britcoin stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock2price[0]) * howmuch
            if ownedstock2[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock2[0] = ownedstock2[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1
        
        if whatstock.lower() == "silicon" :
            howmuch = int(input("how many Silicon Mountain stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Silicon Mountain stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Silicon Mountain stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock3price[0]) * howmuch
            if ownedstock3[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock3[0] = ownedstock3[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "obelisk" :
            howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock4price[0]) * howmuch
            if ownedstock4[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock4[0] = ownedstock4[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "corka cola" :
            howmuch = int(input("how many Corka Cola stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Corka Cola stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Corka Cola stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock5price[0]) * howmuch
            if ownedstock5[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock5[0] = ownedstock5[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "popsi" :
            howmuch = int(input("how many Popsi stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Popsi stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Popsi stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock6price[0]) * howmuch
            if ownedstock6[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock6[0] = ownedstock6[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "haunted house" :
            howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock7price[0]) * howmuch
            if ownedstock7[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock7[0] = ownedstock7[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "dolphin" :
            howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock8price[0]) * howmuch
            if ownedstock8[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock8[0] = ownedstock8[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1


def incrementtime() :
    global money
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price, price1change)
        cryptopricechange(stock2price, price2change)
        mediumconpricechange(stock7price, fakevar1, price7change)
        mediumconpricechange(stock8price, fakevar1, price8change)

        if confidence3[0] < 25 :
            lowconpricechange(stock3price, confidence3, price3change)
        elif confidence3[0] > 75 :
            highconpricechange(stock3price, confidence3, price3change)
        else :
            mediumconpricechange(stock3price, confidence3 , price3change)

        if confidence4[0] < 25 :
            lowconpricechange(stock4price, confidence4, price4change)
        elif confidence4[0] > 75 :
            highconpricechange(stock4price, confidence4, price4change)
        else :
            mediumconpricechange(stock4price, confidence4, price4change)

        if confidence5[0] < 25 :
            lowconpricechange(stock5price, confidence5, price5change)
        elif confidence5[0] > 75 :
            highconpricechange(stock5price, confidence5, price5change)
        else :
            mediumconpricechange(stock5price, confidence5, price5change)

        if confidence6[0] < 25 :
            lowconpricechange(stock6price, confidence6, price6change)
        elif confidence6[0] > 75 :
            highconpricechange(stock6price, confidence6, price6change)
        else :
            mediumconpricechange(stock6price, confidence6, price6change)

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        money = money + 20
        while fakevar2 != 5 :
            bluechippricechange(stock1price, price1change)
            cryptopricechange(stock2price, price2change)
            mediumconpricechange(stock7price, fakevar1, price7change)
            mediumconpricechange(stock8price, fakevar1, price8change)

            if confidence3[0] < 25 :
                lowconpricechange(stock3price, confidence3, price3change)
            elif confidence3[0] > 75 :
                highconpricechange(stock3price, confidence3, price3change)
            else :
                mediumconpricechange(stock3price, confidence3, price3change)

            if confidence4[0] < 25 :
                lowconpricechange(stock4price, confidence4, price4change)
            elif confidence4[0] > 75 :
                highconpricechange(stock4price, confidence4, price4change)
            else :
                mediumconpricechange(stock4price, confidence4, price4change)

            if confidence5[0] < 25 :
                lowconpricechange(stock5price, confidence5, price5change)
            elif confidence5[0] > 75 :
                highconpricechange(stock5price, confidence5, price5change)
            else :
                mediumconpricechange(stock5price, confidence5, price5change)

            if confidence6[0] < 25 :
                lowconpricechange(stock6price, confidence6, price6change)
            elif confidence6[0] > 75 :
                highconpricechange(stock6price, confidence6, price6change)
            else :
                mediumconpricechange(stock6price, confidence6, price6change)

            fakevar2 = fakevar2 + 1
        hour[0] = 1

def easyincrementtime() :
    global money
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price, price1change)
        cryptopricechange(stock2price, price2change)
        mediumconpricechange(stock7price, fakevar1, price7change)
        mediumconpricechange(stock8price, fakevar1, price8change)

        if confidence3[0] < 25 :
            easylowconpricechange(stock3price, confidence3, price3change)
        elif confidence3[0] > 75 :
            easyhighconpricechange(stock3price, confidence3, price3change)
        else :
            easymediumconpricechange(stock3price, confidence3, price3change)

        if confidence4[0] < 25 :
            easylowconpricechange(stock4price, confidence4, price4change)
        elif confidence4[0] > 75 :
            easyhighconpricechange(stock4price, confidence4, price4change)
        else :
            easymediumconpricechange(stock4price, confidence4, price4change)

        if confidence5[0] < 25 :
            easylowconpricechange(stock5price, confidence5, price5change)
        elif confidence5[0] > 75 :
            easyhighconpricechange(stock5price, confidence5, price5change)
        else :
            easymediumconpricechange(stock5price, confidence5, price5change)

        if confidence6[0] < 25 :
            easylowconpricechange(stock6price, confidence6, price6change)
        elif confidence6[0] > 75 :
            easyhighconpricechange(stock6price, confidence6, price6change)
        else :
            easymediumconpricechange(stock6price, confidence6, price6change)

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        money = money + 40
        while fakevar2 != 5 :
            bluechippricechange(stock1price, price1change)
            cryptopricechange(stock2price, price2change)
            mediumconpricechange(stock7price, fakevar1, price7change)
            mediumconpricechange(stock8price, fakevar1, price8change)

            if confidence3[0] < 25 :
                easylowconpricechange(stock3price, confidence3, price3change)
            elif confidence3[0] > 75 :
                easyhighconpricechange(stock3price, confidence3, price3change)
            else :
                easymediumconpricechange(stock3price, confidence3, price3change)

            if confidence4[0] < 25 :
                easylowconpricechange(stock4price, confidence4, price4change)
            elif confidence4[0] > 75 :
                easyhighconpricechange(stock4price, confidence4, price4change)
            else :
                easymediumconpricechange(stock4price, confidence4, price4change)

            if confidence5[0] < 25 :
                easylowconpricechange(stock5price, confidence5, price5change)
            elif confidence5[0] > 75 :
                easyhighconpricechange(stock5price, confidence5, price5change)
            else :
                easymediumconpricechange(stock5price, confidence5, price5change)

            if confidence6[0] < 25 :
                easylowconpricechange(stock6price, confidence6, price6change)
            elif confidence6[0] > 75 :
                easyhighconpricechange(stock6price, confidence6, price6change)
            else :
                easymediumconpricechange(stock6price, confidence6, price6change)

            fakevar2 = fakevar2 + 1
        hour[0] = 1

def hardincrementtime() :
    global money
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price, price1change)
        cryptopricechange(stock2price, price2change)
        mediumconpricechange(stock7price, fakevar1, price7change)
        mediumconpricechange(stock8price, fakevar1, price8change)

        if confidence3[0] < 25 :
            hardlowconpricechange(stock3price, confidence3, price3change)
        elif confidence3[0] > 75 :
            hardhighconpricechange(stock3price, confidence3, price3change)
        else :
            hardmediumconpricechange(stock3price, confidence3, price3change)

        if confidence4[0] < 25 :
            hardlowconpricechange(stock4price, confidence4, price4change)
        elif confidence4[0] > 75 :
            hardhighconpricechange(stock4price, confidence4, price4change)
        else :
            hardmediumconpricechange(stock4price, confidence4, price4change)

        if confidence5[0] < 25 :
            hardlowconpricechange(stock5price, confidence5, price5change)
        elif confidence5[0] > 75 :
            hardhighconpricechange(stock5price, confidence5, price5change)
        else :
            hardmediumconpricechange(stock5price, confidence5, price5change)

        if confidence6[0] < 25 :
            hardlowconpricechange(stock6price, confidence6, price6change)
        elif confidence6[0] > 75 :
            hardhighconpricechange(stock6price, confidence6, price6change)
        else :
            hardmediumconpricechange(stock6price, confidence6, price6change)

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        money = money + 10
        while fakevar2 != 5 :
            bluechippricechange(stock1price, price1change)
            cryptopricechange(stock2price, price2change)
            mediumconpricechange(stock7price, fakevar1, price7change)
            mediumconpricechange(stock8price, fakevar1, price8change)

            if confidence3[0] < 25 :
                hardlowconpricechange(stock3price, confidence3, price3change)
            elif confidence3[0] > 75 :
                hardhighconpricechange(stock3price, confidence3, price3change)
            else :
                hardmediumconpricechange(stock3price, confidence3, price3change)

            if confidence4[0] < 25 :
                hardlowconpricechange(stock4price, confidence4, price4change)
            elif confidence4[0] > 75 :
                hardhighconpricechange(stock4price, confidence4, price4change)
            else :
                hardmediumconpricechange(stock4price, confidence4, price4change)

            if confidence5[0] < 25 :
                hardlowconpricechange(stock5price, confidence5, price5change)
            elif confidence5[0] > 75 :
                hardhighconpricechange(stock5price, confidence5, price5change)
            else :
                hardmediumconpricechange(stock5price, confidence5, price5change)

            if confidence6[0] < 25 :
                hardlowconpricechange(stock6price, confidence6, price6change)
            elif confidence6[0] > 75 :
                hardhighconpricechange(stock6price, confidence6, price6change)
            else :
                hardmediumconpricechange(stock6price, confidence6, price6change)

            fakevar2 = fakevar2 + 1
        hour[0] = 1

def whatcommand() :
    global day
    global hour
    global money
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global clockrec
    global clocktext
    global clocktexttext
    global moneyrec
    global moneytext
    global moneytexttext
    
    buyrec.setFill(color_rgb(0,0,0))
    buyrec.draw(win1)

    buytext.setTextColor(color_rgb(255,255,255))
    buytext.setSize(24)
    buytext.draw(win1)

    sellrec.setFill(color_rgb(0,0,0))
    sellrec.draw(win1)

    selltext.setSize(24)
    selltext.draw(win1)

    statusrec.setFill(color_rgb(0,0,0))
    statusrec.draw(win1)

    statustext.setTextColor(color_rgb(255,255,255))
    statustext.setSize(24)
    statustext.draw(win1)

    timerec.setFill(color_rgb(0,0,0))
    timerec.draw(win1)

    timetext.setTextColor(color_rgb(255,255,255))
    timetext.setSize(24)
    timetext.draw(win1)
    
    clockrec.setFill(color_rgb(0,0,0))
    clockrec.draw(win1)

    clocktext.setTextColor(color_rgb(255,255,255))
    clocktext.setSize(16)
    clocktext.draw(win1)
    
    moneyrec.setFill(color_rgb(0,0,0))
    moneyrec.draw(win1)

    moneytext.setTextColor(color_rgb(255,255,255))
    moneytext.setSize(16)
    moneytext.draw(win1)

    mouse = 0
    mouse = win1.getMouse()
    mousex = mouse.getX()
    mousey = mouse.getY()

    if mousex >=50 and mousex <= 250 and mousey >= 50 and mousey <= 150 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        buy()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >= 50 and mousex <= 250 and mousey >= 200 and mousey <= 300 :
        sell()
    elif mousex >=50 and mousex <= 250 and mousey >= 350 and mousey <= 450 :
        showinfo() #change to show info
    elif mousex >=50 and mousex <= 250 and mousey >= 500 and mousey <= 600 :
        incrementtime()
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        clocktext.undraw()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0]) ]
        clocktext = Text(clockpt3, clocktexttext)
    else : #help command
        pass

def easywhatcommand() :
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
        easyincrementtime()
    elif command.lower() == "time" :
        whattime()
    else : #help command
        stockhelp()

def hardwhatcommand() :
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
        hardincrementtime()
    elif command.lower() == "time" :
        whattime()
    else : #help command
        stockhelp()


def easymodegame() :
    game = 1
    global money
    moneygoal = int(1000)
    while game == 1:
        if money < moneygoal :
            easywhatcommand()
        else :
            print("you win")
            game = 0


def mediummodegame() :
    game = 1
    global money
    global moneypt3
    global moneytext
    global moneytexttext
    moneygoal = int(2000)
    moneytexttext = ["$",str(money)]
    moneytext = Text(moneypt3, moneytexttext)
    while game == 1:
        if money < moneygoal :
            moneytexttext = ["$",str(money)]
            moneytext = Text(moneypt3, moneytexttext)
            whatcommand()
        else :
            print("you win")
            game = 0


def hardmodegame() :
    game = 1
    global money
    moneygoal = int(4000)
    while game == 1:
        if money < moneygoal :
            hardwhatcommand()
        else :
            print("you win")
            game = 0


def startgame() :
    global money
    global game
    global goal
    global win1
    win1.setBackground(color_rgb(255,255,255)) #3 boxes ---> easy medium or hard
    intropt = Point(600,300)
    introtext = Text(intropt, "Welcome to The Miniture Stock Market Game by SPDC Technologies.")
    introtext.setTextColor(color_rgb(0,0,0))
    introtext.setSize(24)
    introtext.draw(win1)
    intropt2 = Point(600,450)
    introtext2 = Text(intropt2, "Click to Continue")
    introtext2.setTextColor(color_rgb(0,0,0))
    introtext2.setSize(16)
    introtext2.draw(win1)
    win1.getMouse()
    introtext.undraw()
    introtext2.undraw()
    easypt1 = Point(80,150)
    easypt2 = Point(380,550)
    easypt3 = Point(230,350)
    easyrec = Rectangle(easypt1, easypt2)
    easyrec.setFill(color_rgb(0,0,0))
    easyrec.draw(win1)
    easytext = Text(easypt3,"Easy Mode")
    easytext.setTextColor(color_rgb(255,255,255))
    easytext.setSize(36)
    easytext.draw(win1)
    mediumpt1 = Point(450,150)
    mediumpt2 = Point(750,550)
    mediumpt3 = Point(600,350)
    mediumrec = Rectangle(mediumpt1, mediumpt2)
    mediumrec.setFill(color_rgb(0,0,0))
    mediumrec.draw(win1)
    mediumtext = Text(mediumpt3, "Normal Mode")
    mediumtext.setTextColor(color_rgb(255,255,255))
    mediumtext.setSize(36)
    mediumtext.draw(win1)
    hardpt1 = Point(820,150)
    hardpt2 = Point(1120,550)
    hardpt3 = Point(970,350)
    hardrec = Rectangle(hardpt1, hardpt2)
    hardrec.setFill(color_rgb(0,0,0))
    hardrec.draw(win1)
    hardtext = Text(hardpt3, "Hard Mode")
    hardtext.setTextColor(color_rgb(255,255,255))
    hardtext.setSize(36)
    hardtext.draw(win1)
    gamemode = win1.getMouse()
    gamemodex = gamemode.getX()
    gamemodey = gamemode.getY()
    goal = 0
    while game != 1 :
        if gamemodex <= 380 and gamemodex >= 80 and gamemodey <= 550 and gamemodey >= 150 :
            easyrec.undraw()
            easytext.undraw()
            mediumrec.undraw()
            mediumtext.undraw()
            hardrec.undraw()
            hardtext.undraw()
            money = 300
            easymodegame()
            game = 1
        elif gamemodex <= 750 and gamemodex >= 450 and gamemodey <= 550 and gamemodey >= 150 :
            easyrec.undraw()
            easytext.undraw()
            mediumrec.undraw()
            mediumtext.undraw()
            hardrec.undraw()
            hardtext.undraw()
            money = 200
            mediummodegame()
            game = 1
        elif gamemodex <= 1120 and gamemodex >= 820 and gamemodey <= 550 and gamemodey >= 150 :
            easyrec.undraw()
            easytext.undraw()
            mediumrec.undraw()
            mediumtext.undraw()
            hardrec.undraw()
            hardtext.undraw()
            money = 100
            hardmodegame()
            game = 1
        else :
            gamemode = win1.getMouse()
            gamemodex = gamemode.getX()
            gamemodey = gamemode.getY()


startgame()