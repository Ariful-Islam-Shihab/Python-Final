from person import *
from Bank import *

abc=Bank("ABC Bank","Banasree",1000000000)


print(f"******************Welcome to {abc.name}*******************")

def frontScreen(bank):
    print("1. Create Admin Account")
    print("2. Admin Log in")
    print("3. User Log in")
    print("4. Exit")
    a=int(input("Enter option: "))
    return a

def userPage(user,bank):
    print(f"\tWeclome {user.name}")
    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Loan")
        print("4. Payback Loan")
        print("5. Transfer to another account")
        print("6. Transaction History")
        print("7. Account info")
        print("8. Exit")
        print()
        a=int(input("Chose Option "))
        if a==1:
            amount=int(input("Enter amount:"))
            user.withdraw(amount,bank)
        elif a==2:
            amount=int(input("Enter amount:"))
            user.deposit(amount,bank)
        elif a==3:
            amount=int(input("Enter amount:"))
            user.takeLoan(bank,amount)
        elif a==4:
            amount=int(input("Enter amount:"))
            user.payBackLoan(bank,amount)
        elif a==5:
            amount=int(input("Enter amount:"))
            accountNumber=int(input("Enter account number:"))
            user.transfer(accountNumber,amount,bank)
        elif a==6:
            user.transactionHistory()
        elif a==7:
            print(user)
        else:
            return




def userLogin(bank):
    number=int(input("Enter account Number: "))
    for i in bank.accounts:
        if i.accountNumber==number:
            return i
    return None



def createAdminAccount(bank):
    name=input("Enter name: ")
    address=input("Enter address: ")
    email=input("Enter email: ")
    password=input("Enter password: ")
    ad=Admin(name,email,address,password)
    bank.addAdmin(ad)

def adminLogin(bank):
    name=input("Enter name: ")
    password=input("Emter Password: ")
    for i in bank.admins:
        if i.name==name and i.password==password:
            return i
        
    return None

def createAnAccount():
    name=input("Enter name: ")
    address=input("Enter address: ")
    email=input("Enter email: ")
    accountType=input("Enter Account type: ")
    acc=User(name,email,address,accountType)
    return acc
    


def adminPage(abc,admin):
    print(f"\tWelcome Admin: {admin.name}")
    while True:
        print("1. Create an account")
        print("2. Remove a account")
        print("3. See all account")
        print("4. Check total balance of bank")
        print("5. Check loan amount of bank")
        print("6. Turn on Loan feature")
        print("7. Turn off Loan feature")
        print("8. Exit")
        print()
        a=int(input("Choose an option: "))
        if a==1:
            account=createAnAccount()
            admin.addAccount(account,abc)
        elif a==2:
            acNumber=int(input("Enter account number: "))
            admin.deleteAccount(acNumber,abc)
        elif a==3:
            admin.seeAllaccounts(abc)
        elif a==4:
            admin.balanceOfBank(abc)
        elif a==5:
            admin.totalLoanAmount(abc)
        elif a==6:
            admin.turnOnLoan(abc)
        elif a==7:
            admin.turnOffLoan(abc)
        elif a==8:
            return



while True:
    a=frontScreen(abc)
    if a==1:
        createAdminAccount(abc)
    elif a==2:
        admin=adminLogin(abc)
        if admin:
            adminPage(abc,admin)
        else:
            print("Invalid Id or Password")
    elif a==3:
        user=userLogin(abc)
        if user:
            userPage(user,abc)
        else:
            print("Invalid account")
    else:
        break