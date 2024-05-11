from user import User,Customer,Admin
from bank import Bank
import datetime

bank=Bank("Bangladesh bank","Dhaka")
def customer_choice(customer):
    while True:
            print("1. Deposit")
            print("2. Widraw")
            print("3. Check Balance")
            print("4. check Transaction History")
            print("5. Take Loan")
            print("6. Repay Loan")
            print("7. Transfer Money")
            print("8. Exit ")

            choice=int(input("Enter your choice : "))
            if choice==1:
                dep_amount=int(input("Deposit Amount: "))
                customer.deposit_amount(dep_amount,bank)
            elif choice==2:
                wid_amount=int(input("Widraw Amount: "))
                customer.widraw_amount(wid_amount,bank)
            elif choice==3:
                customer.check_balance()
            elif choice==4:
                customer.check_transaction_history()
            elif choice==5:
                loan_amount=int(input("Loan Amount: "))
                customer.take_loan(loan_amount,bank)
            elif choice==6:
                repay_amount=int(input("Repay Amount: "))
                customer.repay_loan(repay_amount,bank)
            elif choice==7:
                transfer_amount=int(input("Transfer Amount: "))
                customer2_name=input("Desired account name: ")
                customer2_email=input("Desired account email: ")
                customer2_address=input("Desired account address: ")
                # customer2_acc_type=input("Desired account type(savings/current): ")
                # customer2=Customer(customer2_name,customer2_email,customer2_address,customer2_acc_type)
                flag=True
                for obj in bank.user_archive:
                    if obj.name==customer2_name and obj.email==customer2_email:
                        customer.transfer_amount(obj,transfer_amount)
                        print("Your Transfer is successful")
                        flag=False
                if flag==True:
                    print("Failed!!! Your desired bank account dosem't exist")
            elif choice==8:
                break
            else:
                print("Invalid Choice")

def admin_choice(admin):
    while True:
        print("1. Delete User")
        print("2. See all user")
        print("3. Total Available balace of Bank")
        print("4. Total Loan Amount")
        print("5. Loan Feature on")
        print("6.Loan feature off")
        print("7. Exit ")

        choice=int(input("Enter your choice : "))
        if choice==1:
            user_name=input("User name:")
            user_email=input("User email:")
            admin.delete_user(user_name,user_email,bank)
        elif choice==2:
            admin.see_all_user(bank)
        elif choice==3:
            admin.total_available_balance_of_bank(bank)
        elif choice==4:
            admin.total_loan_amount(bank)
        elif choice==5:
            admin.loan_feature_on(bank)
        elif choice==6:
            admin.loan_feature_off(bank)
        elif choice==7:
            break
        else:
            print("Invalid Choice")
        



def customerr(type):
    print("Thank you for choosing our bank !!!\n")
    name=input("Enter Your name: ")
    email=input("Enter Your email: ")
    flag=True
    if type=="old":
        if len(bank.user_archive)>0:
            for object in bank.user_archive:
                if object.name==name and object.email==email:
                    customer_choice(object)
                    flag=False
        if flag==True:
                print("Invalid user account")
    else:        
        address=input("Enter Your address: ")
        account_type=input("Enter Your account type savings/current: ")
        customer=Customer(name=name,email=email,address=address,account_type=account_type)
        bank.user_archive.append(customer)
        print(f"Congratulation {customer.name} your account is created!! ")
        customer_choice(customer)
        
    
def admin():
    print("Welcome to admin space\n")
    add=int(input("1. Admin login.\n2.New admin account open"))
    name=input("Enter Your name: ")
    email=input("Enter Your email: ")
    address=input("Enter Your address: ")
    if add==2:
        admin=Admin(name=name,email=email,address=address)
        bank.admin_panel.append(admin)
        print(f"Congratulation {admin.name} your account is created!! ")
        admin_choice(admin)
    elif add==1:
        flag=False
        if len(bank.admin_panel)==0:
            flag=False
        else:
            for object in bank.admin_panel:
                if object.name==name and object.email==email and object.address==address:
                    flag=True
                    admin_choice(object)

        if flag==False:
                print("Invalid admin account")
    else:
        print("Invalid Choice")
        
        



while True:
    print(f"*** Welcome to {bank.name}!! ***")
    print("1. Account Holder")
    print("2. Admin")
    print("3. New account open")
    print("4. Exit")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        customerr("old")
    elif choice==2:
        admin()
    elif choice==3:
        customerr("new")
    elif choice==4:
        break
    else:
        print("Invalid Input")