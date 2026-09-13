# Object-Oriented Programming
# Base Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")


# Inheritance
class Student(Person):

    def __init__(self, name, age, branch):

        super().__init__(name, age)

        self.branch = branch

    def study(self):
        print(f"{self.name} is studying {self.branch}.")


student = Student(
    "Rafey",
    21,
    "Computer Science"
)

student.introduce()

student.study()


# Encapsulation

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder

        # Conventionally private attribute
        self._balance = balance

    def deposit(self, amount):

        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance


account = BankAccount(
    "Rafey",
    10000
)

account.deposit(5000)

print("\nBalance:", account.get_balance())