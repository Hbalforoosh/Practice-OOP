class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
            print("updated")
        else:
            print("Error")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit by {amount}. New balance: {self.__balance}")
        else:
            print("Error deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw by {amount}. New balance: {self.__balance}")
        else:
            print("error withdraw")


b1 = BankAccount(15000)
print(f"Current balance: {b1.balance}")
b1.deposit(5000)
b1.withdraw(2000)
b1.withdraw(20000)
b1.balance = -100
b1.balance = 10000
