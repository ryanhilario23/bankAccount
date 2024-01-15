class BankAccount:
    # don't forget to add some default values for these parameters!
    existing_user = []
    def __init__(self, int_rate, balance): 
        
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.existing_user.append(self)
        # don't worry about user info here; we'll involve the User class soon
# Depositing money to balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit sucessful: ${amount}")
        return self
#Withdraw from balance
    def withdraw(self, amount):
    #insuffient funds if goes under
        if (self.balance - amount) < 0:
            print("insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    #suffient funds is OK
        else:
            self.balance -= amount
            print(f"Withdraw Sucessful: ${amount}")
        return self
#Display Bank Acount Balance
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
#Updated balance w/ interest
    def yield_interest(self):
        interest_gained = round(self.balance * self.int_rate,2)
        self.balance += interest_gained
        print(f"Yeild interest: ${interest_gained}\nNew Balance: ${self.balance}")
        return self
    @classmethod
    def active_users(cls):
        for users in cls.existing_user:
            users.display_account_info()


print("Tadashi Hamada")
Tadashi_Hamada = BankAccount(.0435,15)
Tadashi_Hamada.deposit(5).deposit(5).deposit(5).withdraw(40).yield_interest().display_account_info()
print("----------")
print("Hiro Hamada")
Hiro_Hamada = BankAccount(.001, 1510)
Hiro_Hamada.display_account_info().deposit(200).deposit(300).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
print("----------")

BankAccount.active_users()

