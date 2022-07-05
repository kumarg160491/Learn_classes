# using private instance 
class Class_name:
    def __init__(self, a, b):
        self.a = a
        self.__b = b

    def sum(self):
        return self.a + self.__b


c = Class_name(1, 2)
print(c.a)
# print(c.b)
