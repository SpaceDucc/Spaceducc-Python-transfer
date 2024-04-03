from turtle import *
from graphics import *

def test1() :
    win = GraphWin("Mywindow", 1200, 700)
    win.setBackground(color_rgb(255,255,255))
    pt1 = Point(250,250)
    cir1 = Circle(pt1,100)
    cir1.setFill(color_rgb(255,255,0))
    cir1.draw(win)
    pt2 = Point(220,220)
    cir2 = Circle(pt2,15)
    cir2.setFill(color_rgb(0,0,0))
    cir2.draw(win)
    pt3 = Point(280,220)
    cir3 = Circle(pt3,15)
    cir3.setFill(color_rgb(0,0,0))
    cir3.draw(win)
    pt4 = Point(200,270)
    pt5 = Point(300,310)
    ov1 = Oval(pt4,pt5)
    ov1.setFill(color_rgb(0,0,0))
    ov1.draw(win)
    pt6 = Point(200,250)
    pt7 = Point(300,295)
    ov2 = Oval(pt6,pt7)
    ov2.setFill(color_rgb(255,255,0))
    ov2.setOutline(color_rgb(255,255,0))
    ov2.draw(win)
    pt8 = Point(170,180)
    pt9 = Point(330,150)
    rec1 = Rectangle(pt8,pt9)
    rec1.setFill(color_rgb(0,0,0))
    rec1.draw(win)
    pt10 = Point(200,150)
    pt11 = Point(300,50)
    rec2 = Rectangle(pt10,pt11)
    rec2.setFill(color_rgb(0,0,0))
    rec2.draw(win)
    pt12 = Point(200,150)
    pt13 = Point(300,130)
    rec3 = Rectangle(pt12,pt13)
    rec3.setFill(color_rgb(150,150,0))
    rec3.draw(win)

    pt14 = win.getMouse()
    print(pt14)
    

def test2() :
    win1 = GraphWin("Test2", 500,500)
    win1.setBackground(color_rgb(255,255,255))
    pt1 = Point(100,100)
    pt2 = Point(200,200)
    rec1 = Rectangle(pt1,pt2)
    rec1.setFill(color_rgb(0,0,0))
    rec1.draw(win1)
    click1 = win1.getMouse()
    x1 = click1.getX()
    y1 = click1.getY()
    if x1 >= 100 and y1 >= 100 and x1 <= 200 and y1 <= 200 :
        print("yay")
    else :
        print("nay")
    
    win1.getMouse()
    win1.close()
    
def test3() :
    day = [1]
    hour = [1]
    game = 1

    win1 = GraphWin("MSMG", 1200, 700)
    win1.setBackground(color_rgb(255,255,255))

    buypt1 = Point(50,50)
    buypt2 = Point(250,150)
    buyrec = Rectangle(buypt1,buypt2)
    buyrec.setFill(color_rgb(0,0,0))
    buyrec.draw(win1)

    buypt3 = Point(150,100)
    buytext = Text(buypt3, "Buy Stock")
    buytext.setTextColor(color_rgb(255,255,255))
    buytext.setSize(24)
    buytext.draw(win1)

    sellpt1 = Point(50,200)
    sellpt2 = Point(250,300)
    sellrec = Rectangle(sellpt1,sellpt2)
    sellrec.setFill(color_rgb(0,0,0))
    sellrec.draw(win1)

    sellpt3 = Point(150,250)
    selltext = Text(sellpt3, "Sell Stock")
    selltext.setTextColor(color_rgb(255,255,255))
    selltext.setSize(24)
    selltext.draw(win1)

    statuspt1 = Point(50,350)
    statuspt2 = Point(250,450)
    statusrec = Rectangle(statuspt1,statuspt2)
    statusrec.setFill(color_rgb(0,0,0))
    statusrec.draw(win1)

    statuspt3 = Point(150,400)
    statustext = Text(statuspt3, "Information")
    statustext.setTextColor(color_rgb(255,255,255))
    statustext.setSize(24)
    statustext.draw(win1)

    timept1 = Point(50,500)
    timept2 = Point(250,600)
    timerec = Rectangle(timept1,timept2)
    timerec.setFill(color_rgb(0,0,0))
    timerec.draw(win1)

    timept3 = Point(150,550)
    timetext = Text(timept3, "Next Hour")
    timetext.setTextColor(color_rgb(255,255,255))
    timetext.setSize(24)
    timetext.draw(win1)

    clockpt1 = Point(1000,25)
    clockpt2 = Point(1100,75)
    clockrec = Rectangle(clockpt1,clockpt2)
    clockrec.setFill(color_rgb(0,0,0))
    clockrec.draw(win1)

    clockpt3 = Point(1050,50)
    clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0])]
    clocktext = Text(clockpt3, clocktexttext)
    clocktext.setTextColor(color_rgb(255,255,255))
    clocktext.setSize(16)
    clocktext.draw(win1)

    while game != 0 :
        win1.getMouse()
        day[0] = day[0] + 1
        hour[0] = hour[0] + 1
        clocktext.undraw()
        clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0])]
        clocktext = Text(clockpt3, clocktexttext)
        clocktext.setTextColor(color_rgb(255,255,255))
        clocktext.setSize(16)
        clocktext.draw(win1)


    win1.getMouse()

test3()

