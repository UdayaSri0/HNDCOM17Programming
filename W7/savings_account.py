from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=5.0):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest {self.interest_rate}. New balance: {self.balance}")