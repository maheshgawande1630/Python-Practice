#Create Account class with 2 attributes- balance and account no:
#create methods for debit,credit and printing the balance

class Account:

    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_no = acc_no
    
    def debit(self, amount):

        if amount > self.balance:
            print("Insufficient Balance")
            return

        if amount <= 0:
            print("Invalid Input")    
            return

        self.balance -= amount
        print(f"Account {self.account_no} is debited by {amount}")

    def credit(self, amount):

        if amount <= 0:
            print("Invalid Input")
            return

        self.balance += amount
        print(f"Account {self.account_no} is credited by {amount}")

    def total_bal(self):
        print(f"Total balance of {self.account_no} is {self.balance}")
        

Acc_1 = Account (10000,12345)
Acc_1.debit(2000)
Acc_1.credit(3000)
Acc_1.total_bal()