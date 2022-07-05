class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area()

    def area(self):
        Area = self.length * self.breadth
        Perimeter = 2 * (self.length + self.breadth)
        print('Area:', Area)
        print('Perimter:', Perimeter)


rect1 = Rectangle(3, 4)
rect2 = Rectangle(4, 5)

# rect1.area()
# rect2.area()
