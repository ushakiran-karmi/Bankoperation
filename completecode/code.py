#creating account
class Bank:
    bank="SBI"
    branch="koutala"
    
    
    def __init__(self,username,pancard,address):
        self.username=username
        self.pancard=pancard
        self.address=address
        self.accountbalance=00
        print(f"{self.username} account created successfully in SBI Bank")
      
      
    #creating the deposite code    
    def deposit(self,amount):
        self.accountbalance=self.accountbalance+amount
        print(f"{amount} deposite successfully")
        
    #creating withdraw
    def withdraw(self,amount):
        if amount<self.accountbalance:
            self.accountbalance=self.accountbalance-amount
            print(f"{amount} withdraw successfully")
        else:
            print("YOU HAVE INSUFFICIATE BALANCE")
        
    def ministatement(self):
        print(f"your account balance is{self.accountbalance}")    
        

print(f"WELCOME TO THE {Bank.bank} {Bank.branch} ")         
username=input("enter the username: ")
pancard=input("enter the pancard: ")
address=input("enter the address: ")        
        
b=Bank(username,pancard,address)  


while True:
    print("PLEASE SELECT ANY ABOVE OPTION")
    print("1.Deposite\n2.Withdraw\n3.Ministatement\n4.Stop")
    option=int(input("  "))
    
    if option ==1:
        amount=float(input("enter the deposit amount: "))
        b.deposit(amount)
        
    elif option ==2:
        amount=float(input("enter the withdraw amount:   "))
        b.withdraw(amount)
        
    elif option ==3:
        b.ministatement()    
    elif option ==4:
        print("Thank for using the SBI Bank account for transiction")
        break
    else:
        print("You entered wrong option")
