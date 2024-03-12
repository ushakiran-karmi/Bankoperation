#withdraw
def withdraw(self,amount):
    if amount<self.accountbalance-amount:
        print(f"{amount} withdraw successfully")
        
    else:
        print("YOUR ACCOUNT HAS INSUFFICIATE BALANCE")    
        
        
if option ==2:
    amount=float(input("enter the withdraw amount" ))   
    b.withdraw(amount)     