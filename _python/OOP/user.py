class user:
    def __init__(self, name):
        self.name = name
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

Hani = user("Hani")
Hani.make_deposit(11100)
Hani.make_deposit(540)
Hani.make_deposit(200)
Hani.make_withdrawal(220)
Hani.display_user_balance()

nizam = user("nizam")
nizam.make_deposit(500)
nizam.make_deposit(150)
nizam.make_withdrawal(320)
nizam.make_withdrawal(700)
nizam.display_user_balance()

Hala = user("Hala")
Hala.make_deposit(1000)
Hala.make_deposit(400)
Hala.make_withdrawal(50)
Hala.make_withdrawal(50)
Hala.display_user_balance()


nizam.transfer_money(Hani, 400)
Hani.display_user_balance()
nizam.display_user_balance()