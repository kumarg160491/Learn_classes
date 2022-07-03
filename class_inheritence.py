class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)


class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, id_number)

    def employee_details(self):
        print('The name of the employee is {0} and his/her id number is {1} with salary {2} and working as {3}.'.format(
            self.name, self.id_number, self.salary, self.post))


a = Employee('Rahul', 2548, 59000, 'Software Engineer')
a.display()
a.employee_details()
