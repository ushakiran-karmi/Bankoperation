#Deposit
def deposit(self,amount):
    self.balance=self.balance+amount
    print(f'{amount} deposited successfully')
    
while True:
    print("please select any option:")
    print("1.Deposit\n2.Withdraw\n3.Ministatement\n4.stop")
    option=int(input(""))
    
    
    if option=='1':
        amount=float(input('Enter the Deposit amount'))
        b.deposit()
    if option=='4':
        print("Thank you for using SBI bank for transiction")    
