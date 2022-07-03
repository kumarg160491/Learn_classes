# decorator function - expression gets evaluated after function is defined
# instance, class and static method

from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('Gaurav', 31)
print('and the name is ', __name__)
if __name__ == '__main__':
    person2 = Person.fromBirthYear('Gaurav', 1991)
    print(person1.age)
    print(person2.age)


