class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
tyler = User("Tyler Knight", "tdog9001@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

# 3 Deposits, 1 Withdraw

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance()

# 2 Deposits, 2 Withdraws

monty.make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# 1 Deposits, 3 Withdraws

tyler.make_deposit(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

# Transfer Money

guido.transfer_money(tyler,100).display_user_balance()
tyler.display_user_balance()