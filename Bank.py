class Bank:
    def __init__(self,name,address,balance) -> None:
        self.name=name
        self.address=address
        self.balance=balance
        self.admins=[]
        self.accounts=[]
        self.loanFeature=True
        self.loanAmount=0
    
    def addAdmin(self,admin):
        self.admins.append(admin)
    
    def deleteAdmin(self,admin):
        self.admins.remove(admin)