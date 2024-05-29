import datetime
class Person:
    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address

class User(Person):
    def __init__(self, name, email, address,accountType) -> None:
        super().__init__(name, email, address)
        self.__accountType=accountType
        self.balance=0
        self.loan=0
        self.loanAmount=0
        self.transactionhistory=[]
    def withdraw(self,amount,bank):
        if self.balance<=0:
            print("\tPlease pay your debt first")
            print(f"\tYour current dept is {-self.balance}")

        elif self.balance<amount:
            print("--------Withdraw limit exceeded----------")
        elif bank.balance<amount and self.balance>=amount:
            print("--------Bank is bankrupt----------")
        
        else:
            print("\t---------Withdraw Successful----------")
            self.balance-=amount
            bank.balance-=amount
            self.transactionhistory.append(f"Withdraw of {amount} has been made at {datetime.time()}")
    
    def takeLoan(self,bank,amount):
        if self.loan>=2:
            print("Loan time exceeded")
        elif bank.loanFeature==False:
            print("Loan feature is currently off")
        elif bank.balance<amount:
            print("\tBank doen't have enough balance")
        else:
            print(f"Loan of {amount} has been recieved successfully")
            self.balance+=amount
            self.loan+=1
            bank.balance-=amount
            bank.loanAmount+=amount
            self.transactionhistory.append(f"Loan of {amount} has been made at {datetime.time()}")
    def payBackLoan(self,bank,amount):
        if self.loan<=0 and self.balance>=0:
            print("\tYou didn't take any loan")
        else:
            print("*****************Thank you*****************")
            self.transactionhistory.append(f"Loan Payment of {amount} has been made at {datetime.time()}")
            self.loanAmount-=amount
            bank.loanAmount-=amount
            bank.balance+=amount
            self.loan-=1

    def deposit(self,amount,bank):
        if amount<=0:
            print("--------------Invalid amount----------------")
        else:
            print("---------------Deposit Successful-----------")
            self.balance+=amount
            self.transactionhistory.append(f"Deposit of {amount} has been made at {datetime.time()}")
            bank.balance+=amount
    def transfer(self,accountNumber,amount,bank):
        account=Admin.search(bank,accountNumber)
        if bank.accounts.count(account)==0:
            print("-----------------Account doesnot exist--------------")
        else:
            print(f"Transfer of {amount} has been made from {self.name} to {account.name}")
            self.balance-=amount
            account.balance+=amount
            self.transactionhistory.append(f"Transfer of {amount} has been made at {datetime.time()} from: {self.accountNumber} to: {account.accountNumber}")
            account.transactionhistory.append(f"Transfer of {amount} has been made at {datetime.time()} from: {self.accountNumber} to: {account.accountNumber}")

    def checkBalance(self):
        print(f"\tCurrent Balance: {self.balance}")

    def __repr__(self) -> str:
        return f"\tName: {self.name}\n\tAddress:{self.address}\n\tEmail: {self.email}\n\tAccount Number: {self.accountNumber}\n\tAccount type: {self.__accountType}\n\tBalance: {self.balance} "
    def transactionHistory(self):
        for i in self.transactionhistory:
            print(i)
    def setAccountNumber(self,a):
        self.accountNumber=a
    def currentBalance(self):
        print(f"Current balance is {self.balance}")
    
class Admin(Person):
    def __init__(self, name, email, address,password) -> None:
        super().__init__(name, email, address)
        self.password=password
    
    def addAccount(self,account,bank):
        print("************Account added successfully*************")
        account.setAccountNumber(int(len(bank.accounts)+1))
        bank.accounts.append(account)
    @staticmethod
    def search(bank,accountNumber):
        for i in bank.accounts:
            if i.accountNumber==accountNumber:
                return i
        return None


    def deleteAccount(self,accountNumber,bank):      
        
        bank.accounts.remove(Admin.search(bank,accountNumber))
        print("************Account deleted successfully*************")
        
    
    def seeAllaccounts(self,bank):
        for i in bank.accounts:
            print(i)

    def balanceOfBank(self,bank):
        print(f"Balance of {bank.name} is {bank.balance}")

    def totalLoanAmount(self,bank):
        print(f"Loan amount of {bank.name} is {bank.loanAmount}")

    def turnOnLoan(self,bank):
        print(f"Loan feature of {bank.name} has been turned on")
        bank.loanFeature=True

    def turnOffLoan(self,bank):
        print(f"Loan feature of {bank.name} has been turned off")
        bank.loanFeature=False