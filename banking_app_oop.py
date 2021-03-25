# Parent Class : User
# Child Class : Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposits, withdrawl, view_balance

# Parent Class
class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Address", self.address)


# Child Class
class Bank(User):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account blanace has been updated : $ ", self.balance)

