class Person:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number



class Employee(Person):
    def __init__(self, name, surname, age, phone_number, id, salary, position, responsabilities):
        Person.__init__(self, name, surname, age, phone_number)
        self.id = id
        self.salary = salary
        self.position = position
        self.responsabilities = responsabilities

class Intern(Person):
    def __init__(self, name, surname, age, phone_number, salary, scolarship, menthor):
        Person.__init__(self, name, surname, age, phone_number)
        self.salary = salary
        self.scolarship = scolarship
        self.menthor = menthor


def main():



if __name__ == '__main__':
