import turtle

def test1(a) :
    if a != 100 :
        turtle1 = turtle.Turtle()
        if a % 20 != 0 :
            x = 1
            while x != 5 :
                turtle1.right(a)
                turtle1.forward(a)
                x = x + 1
        else :
            x = 1
            while x != 5 :
                turtle1.left(a)
                turtle1.forward(a)
                x = x + 1
        a = int(a + 10)
        test1(a)
    else :
        turtle.done()

test1(int(10))