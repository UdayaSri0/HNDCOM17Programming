class BankAccount:
    # Constructor to initialize a bank account with an account holder name and an optional starting balance
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute to store the name of the account holder
        self._balance = balance  # Protected attribute to store the account balance (accessible within class and subclasses)

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:  # Check if the deposit amount is greater than 0
            self._balance += amount  # Add the deposit amount to the current balance
            print(f"Deposited {amount} successfully!")  # Confirmation message for successful deposit
        else:
            print("Invalid deposit amount.")  # Error message for invalid deposit amounts

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:  # Check if withdrawal amount is valid and doesn't exceed the balance
            self._balance -= amount  # Deduct the withdrawal amount from the current balance
            print(f"Withdrew {amount} successfully!")  # Confirmation message for successful withdrawal
        else:
            print("Invalid withdrawal amount.")  # Error message for insufficient funds or invalid withdrawal amounts

    # Method to retrieve the current account balance
    def get_balance(self):
        return self._balance  # Return the current balance
