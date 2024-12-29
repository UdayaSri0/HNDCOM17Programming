#Base class account 
class BankAccount:
    def __init__(self, account_holder=None, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance
    
#Derived class SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate #public attribute
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest. New balance: {self.balance}")

# Derived class CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):  
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


#polymorphism example
def display_account_info(account):
    print(f"Account Holder: {account.account_holder}")
    print(f"Balance: {account.get_balance()}")


#main program using polymorphism to create instances of different account types

def main():
    # Create instances of different account types
    print("===== π bank =====")
    savings_account = SavingsAccount("Supun ", 1000)
    checking_account = CheckingAccount("Sumudu ", 500)

    print("\n[Savings Account opeerations]")
    savings_account.deposit(200)
    savings_account.add_interest()
    display_account_info(savings_account)

    print("\n[Checking Account opeerations]")
    checking_account.withdraw(1500)
    display_account_info(checking_account)

if __name__ == "__main__":
    main()



    