class User:
    def init(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self 


class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = 0.01
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance+(self.balance*self.int_rate) 
        return self   



Hani = BankAccount(0.01,1000)
nizam = BankAccount(0.01,1230)
Hani.deposit(1000).deposit(1000).deposit(1000).withdraw(1500).yield_interest().display_account_info()
nizam.deposit(9800).deposit(10700).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

#make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code
#, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code
