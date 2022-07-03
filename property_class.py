# Encapsulation concept with property decorator

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def percentage(self):
        return (self.__marks / 600) * 100

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, values):
        self.__marks = values

s = Student(400)
s.marks = 500
print(s.marks)
print(s.percentage())