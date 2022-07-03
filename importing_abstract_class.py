from abstract_class import Shape


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


r = Rectangle(10, 30)
print(r.area())

print(r.__dict__)
