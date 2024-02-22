from turtle import *
from graphics import *

def test1() :
    win = GraphWin("Mywindow", 500, 500)

    win.getMouse()
    win.close()

test1()
def test2() :
    for steps in range(100) :
        for c in ('blue', 'red', 'green') :
            color(c)
            forward(steps)
            right(30)

