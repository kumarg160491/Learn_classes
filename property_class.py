class Student:

    def __init__(self, marks):
        self.marks = marks

    def percentage(self):
        return (self.marks / 600) * 100

    @property
    def marks(self):
        return self.marks

    @marks.setter
    def marks(self, values):
        self.marks = values

s = Student(400)
s.marks = 500
print(s.marks)
print(s.percentage())