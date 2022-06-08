class employee:

    def __init__(self, firstname, lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + '.' + lastname + "@gmail.com"
    def fullname (self):
        return "{} , {}".format(self.firstname , self.lastname)

emp1 = employee('Emanuel', 'maharat', 10000)
emp2 = employee('john', 'sam', 5000)

print(employee.fullname(emp2))


