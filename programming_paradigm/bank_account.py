class BankAccount:
    def __init__(self, account_balance=0):
        self.__accountBalance=account_balance
    def deposit(self, amount):
        self.__accountBalance+=amount
    def withdraw(self, amount):
        if 0 < amount <= self.__accountBalance:
            self.__accountBalance -= amount
            return True
        return False
    def display_balance(self):
        print(f"Current Balance: ${self.__accountBalance:.2f}")