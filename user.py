from random import randint 
from abc import ABC
from datetime import datetime

class User(ABC):
    def __init__(self,name,email,address) -> None:
        super().__init__()
        self.name=name
        self.email=email
        self.address=address


class Customer(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_type=account_type
        self.balance=0
        self.account_number=randint(1000,2000)
        self.transaction_history=[{}]
        self.loan_time=0
        self.loan_balance=0

    def deposit_amount(self,dep_amount,bank):
        if dep_amount>0:
            self.balance+=dep_amount
            bank.total_balance+=dep_amount
            x=datetime.now()
            y=x.strftime("%x")
            self.transaction_history.append({f"Date:{y}": f"Amount Deposited: {dep_amount}"})
            print(f"{dep_amount}Tk Successfully deposited to your account")
        else:
            print("You entered an invalid deposit amount")

    def widraw_amount(self,wid_amount,bank):
        if wid_amount>self.balance:
            print("Withdraw amount exceeded")
        elif wid_amount>bank.total_balance:
            print("Sorry!!! bank is bankrupt.")
        else:
            self.balance-=wid_amount
            bank.total_balance-=wid_amount
            x=datetime.now()
            y=x.strftime("%x")
            self.transaction_history.append({f"Date:{y}": f"Amount Widrwan: {wid_amount}"})
            print(f"{wid_amount}Tk successfully widrawn from your account")

    def check_balance(self):
        print(f"Your available balance: {self.balance}")
    
    def check_transaction_history(self):
        for index in self.transaction_history:
            print(index)

    def take_loan(self,loan_amount,bank):
        if bank.loan_feature_activation==False:
            print("Sorry!!! Your bank dosen't allow loan system")
        elif self.loan_time>=2:
            print("Sorry!! you have already taken loan for maximum time")
        elif loan_amount>2*self.balance:
            print("Sorry !! You only can take loan twice of your current account balance")
        else:
            self.loan_balance+=loan_amount
            bank.total_loan_balance+=loan_amount
            bank.total_balance-=loan_amount
            print(f"Congratulation!! Your {loan_amount}Tk loan granted")
            self.loan_time+=1

    def repay_loan(self,repay_amount,bank):
        if bank.loan_feature_activation==False:
            print("Sorry!!! Your bank dosen't allow loan system")
        elif self.loan_balance<=0:
            print("Sorry!! you do not have any loan to repay")
        else:
            self.loan_balance-=repay_amount
            bank.total_loan_balance-=repay_amount
            bank.total_balance+=repay_amount
            print(f"Congratulation!! You repaid {repay_amount}Tk loan. Your remaining loan amount is: {self.loan_balance}Tk")
        
    def transfer_amount(self,other_account,t_amount):
        if self.balance<t_amount:
            print("Sorry!! you dont have enough balance to transfer")
        else:
            self.balance-=t_amount
            other_account.balance+=t_amount
            print("Successfully Transfered")


class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def delete_user(self,name,email,bank):
        for object in bank.user_archive:
            if object.name==name and object.email==email:
                bank.user_archive.remove(object)

    def see_all_user(self,bank):
        for object in bank.user_archive:
            print(f"Nmae: {object.name} Account Number: {object.account_number} Available Balance: {object.balance}")
    
    def total_available_balance_of_bank(self,bank):
        print(f"Total available balance of bank: {bank.total_balance}")

    def total_loan_amount(self,bank):
        print(f"Total loan balance of bank: {bank.total_loan_balance}")

    def loan_feature_on(self,bank):
        bank.loan_feature_activation=True

    def loan_feature_off(self,bank):
        bank.loan_feature_activation=False
