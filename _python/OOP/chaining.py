class user:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposite(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"user: {self.name}, balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance-=amount
        other_user.account_balance+=amount
        return self

Hani = user("Hani")
Hani.make_deposite(11100).make_deposite(540).make_withdrawal(220).display_user_balance()

nizam = user("nizam")
nizam.make_deposite(500).make_deposite(150).make_withdrawal(320).make_withdrawal(700).display_user_balance()

Hala = user("Hala")
Hala.make_deposite(1000).make_deposite(400).make_withdrawal(50).display_user_balance()

nizam.transfer_money(Hani, 400).Hani.display_user_balance()
nizam.display_user_balance()