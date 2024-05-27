class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

account1 = BankAccount("12345", "Rama H")

account1.deposit(1000)
print("Balance after deposit: $", account1.get_balance())

account1.withdraw(500)
print("Balance after withdrawal: $", account1.get_balance())

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

    def print_info(self):
        print("Current balance: $", self.get_balance())
        print("Interest rate: ", self.interest_rate)

savings_account1 = SavingsAccount("54321", "Rama 2", 0.05)
savings_account1.deposit(2000)
savings_account1.apply_interest()
savings_account1.print_info()