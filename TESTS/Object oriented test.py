import math

class Shape :
    def FindArea(self) :
        pass

    def FindPerimiter(self) :
        pass

class Rectangle(Shape) :
    def __init__(self, hight, width, area, perimiter) :
        self.hight = hight
        self.width = width 
        self.area = area
        self.perimiter = perimiter

    def FindArea(self) :
        self.area = self.hight * self.width
        print("The Area of this rectangle is:", self.area)
    
    def FindPerimiter(self) :
        self.perimiter = (self.hight * 2) + (self.width * 2)
        print("The Perimiter of this rectangle is:", self.perimiter)

class Triangle(Shape) :
    def __init__(self, hight, base, side1, side2, side3, area, perimiter) :
        self.hight = hight
        self.base = base
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area = area
        self.perimiter = perimiter

    def FindArea(self) :
        self.area = self.hight * self.base * 0.5
        print("The Area of this triangle is:", self.area)

    def FindPerimiter(self) :
        self.perimiter = self.side1 + self.side2 + self.side3
        print("The Perimiter of this triangle is:", self.perimiter)

class Circle(Shape) :
    def __init__(self, radius, circumference, area) :
        self.radius = radius
        self.circumference = circumference
        self.area = area

    def FindArea(self) :
        self.area = math.pi * self.radius * self.radius
        print("The Area of this circle is:", self.area)

    def FindPerimiter(self) :
        self.circumference = math.pi * self.radius * 2
        print("The Circumference of this circle is:", self.circumference)



rectangle1 = Rectangle(10, 20, 0, 0)
triangle1 = Triangle(4, 3, 4, 3, 5, 0, 0)
circle1 = Circle(4, 0, 0)

rectangle1.FindArea()
rectangle1.FindPerimiter()
triangle1.FindArea()
triangle1.FindPerimiter()
circle1.FindArea()
circle1.FindPerimiter()