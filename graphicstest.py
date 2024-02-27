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
    win1 = GraphWin("MSMG", 1200, 700)
    win1.setBackground(color_rgb(255,255,255)) #3 boxes ---> easy medium or hard
    easypt1 = Point(80,200)
    easypt2 = Point(380,500)
    easyrec = Rectangle(easypt1, easypt2)
    easyrec.setFill(color_rgb(0,0,0))
    easyrec.draw(win1)
    mediumpt1 = Point(450,200)
    mediumpt2 = Point(750,500)
    mediumrec = Rectangle(mediumpt1, mediumpt2)
    mediumrec.setFill(color_rgb(0,0,0))
    mediumrec.draw(win1)
    hardpt1 = Point(820,200)
    hardpt2 = Point(1120,500)
    hardrec = Rectangle(hardpt1, hardpt2)
    hardrec.setFill(color_rgb(0,0,0))
    hardrec.draw(win1)

    win1.getMouse()
test3()

