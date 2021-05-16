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
    def __init__(self, int_rate=0.01, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount<self.balance:
            self.balance -= amount
        else:
            self.balance -= 5
            print ("Insufficient funds: Charging a $5 fee")
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

