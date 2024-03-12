#creating account
class Bank:
    bank="SBI"
    branch="koutala"
    
    
    def __init__(self,username,pancard,address):
        self.username=username
        self.pancard=pancard
        self.address=address
        self.accountbalance=15000
        
username=input("enter the username")
pancard=input("enter the pancard")
address=input("enter the address")        
        
b=Bank(username,pancard,address)        