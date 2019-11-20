### TEST FUNCTION: test_sort ###

## Define __lt__(self, other) for Employee

class Person:
    "A Person"
    def __init__(self, first, last):
        self.firstname = first.capitalize()
        self.lastname = last.capitalize()

    def __str__(self):
        return self.firstname + " " + self.lastname


class Employee(Person):
    "A Person who is Employed"
    def __init__(self, first, last, company, id):
        # Call Superclass to set common information
        super().__init__(first, last)
        self.id = id
        self.company = company

    def __str__(self):
        # Call Superclass to dispaly common information
        return super().__str__() + ", " + str(self.id) + ' at ' + self.company
    
    def __lt__(self, other):
        lst = []
        lst.append(self)
        lst.append(other)
        sorted(lst, key=lambda k: (employee.company, employee.id))