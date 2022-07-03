class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        self.age = age
        Parent.__init__(self, name)

    def child_age(self):
        return self.age


class Grandchild(Child):
    def __init__(self, name, age, address):
        Parent.__init__(self, name)
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


grand_child = Grandchild('Gaurav', 31, 'Bangalore')
print('The address is', grand_child.get_address(), 'name is', grand_child.name, 'and the age is', grand_child.age)
