#creating account
class Bank:
    bank="SBI"
    branch="koutala"
    
    
    def __init__(self,username,pancard,address):
        self.username=username
        self.pancard=pancard
        self.address=address
        self.accountbalance=15000
        print(f"{self.username} account created successfully in SBI Bank")
        
    def deposit(self,account):
        self.accountbalance=self.accountbalance+account
        print(f"{amount} deposite successfully")
        
        

print(f"WELCOME TO THE {Bank.bank} {Bank.branch} ")         
username=input("enter the username: ")
pancard=input("enter the pancard: ")
address=input("enter the address: ")        
        
b=Bank(username,pancard,address)  


while True():
    print("PLEASE SELECT ANY ABOVE OPTION")
    print("1.Deposite\n2.Withdraw\n3.Ministatement\n4.Stop")
    option=int(print(""))
    
    if option =='1':
        amount=float(print("enter the deposit amount"))
        b.deposit()
    if option =='4':
        print("Thank for using the SBI Bank account for transiction")    