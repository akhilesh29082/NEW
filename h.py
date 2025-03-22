class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}. New Balance: {self.balance}")

# Creating multiple accounts easily
account1 = BankAccount("Alice", 5000)
account2 = BankAccount("Bob", 3000)

account1.deposit(1000)  # Alice deposited 1000. New Balance: 6000
account2.deposit(500)   # Bob deposited 500. New Balance: 3500
