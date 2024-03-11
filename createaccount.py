

class Bank:
    bankname="SBI"
    branch="SBI,KTL,INDIA"
    
    
    #create account
    def __init__(self,username,pancard,address):
        self.username=username
        self.pancard=pancard
        self.address=address
        print("hello {self.username}your account created successfully")

username=input("ENTER YOUR USERNAME:")
pancard=input("ENTER YOUR PANCARD:")
address=input("ENTER YOUR ADDRESS:")

b=Bank(username,pancard,address)        
