class Account:

    def __init__(self,acc_no,acc_name,balance):
        self.account_no=acc_no
        self.account_name=acc_name
        self.account_balance=balance
    

    def display_account_details(self):
        print(f"account name: {self.account_name} account no. {self.account_no} account balance: {self.account_balance}")

class SavingAccount(Account):
    min_balance=1000
    
    def deposit(self,amount):
        if amount<0:
            print("amount can't be negative")
        self.balance=+amount
        print(f"successfully deposited. {amount} current balance is:{self.balance}")
    
    def withdraw(self,amount):
       if not SavingAccount.verify(self.balance,amount):
           print("withdrawl failed. insufficient funds or below minimum balance")
       self.balance-=amount
       print(f"successfully withdrawn {amount} new balance is {self.balance}")
   
    def transfer(self):
        pass
    @classmethod
    def display_min_balance(cls):
        print("minimum balance is:",cls.min_balance)
    @staticmethod
    def verify(current_balance,amount):
        if amount<0:
            return False
        if current_balance-amount<SavingAccount.min_balance:
            return False
        return True
        
obj=SavingAccount(1001,"arunkc",50000)
SavingAccount.display_min_balance()
obj.display_account_details()
obj.withdraw(30000)
