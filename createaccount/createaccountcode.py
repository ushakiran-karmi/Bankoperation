#create account code
class Bank:
    bankname="SBI"
    branch="SBI,KTL,INDIA"
    
    
    #create account
    def __init__(self,username,pancard,address):
        self.username=username
        self.pancard=pancard
        self.address=address
        self.accountbal=15000
        print(f"hello {self.username} account created successfully")

print(f"welcome to the {Bank.bankname} {Bank.branch}")
username=input("ENTER YOUR USERNAME:")
pancard=input("ENTER YOUR PANCARD:")
address=input("ENTER YOUR ADDRESS:")


b=Bank(username,pancard,address)        
