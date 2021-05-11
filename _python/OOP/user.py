class User:
    def init(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

lana = User("lana","lanamail")
nizam = User("nizam","nizamra")
lana.make_deposit(9720)
lana.display_user_balance()
nizam.make_deposit(720)
nizam.display_user_balance()
lana.transfer_money(nizam,4000)
lana.make_deposit(1200)
print(lana.account_balance)
lana.make_withdrawal(2600)
print("after withdrw",lana.account_balance)
lana.display_user_balance()
nizam.display_user_balance()