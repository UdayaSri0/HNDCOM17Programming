from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            print(f"Overdraft limit: {self.overdraft_limit}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")