class BankAcnt:
    def __init__(self, acntnum, name, type, balance=0):
        self.acntnum= acntnum
        self.holdername = name
        self.type= type
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        print("Balance:",self.balance)
    
    def withdraw(self,amount):
        if amount < self.balance:
         self.balance -= amount
         print("Balance:",self.balance)
        else:
            print("Insufficient balance")
    
    def acntdetails(self,acntnum, name, type):
        return f"Account Number: {acntnum}\n Holder Name: {name}\nBalance: {self.balance}"
        
acntnum=78687697689


acntnum=acntnum+1
name=input("enter account holder name:\n")
typ= int(input("select account type:\n1.Savings\n2.Current\n3.Zero\n"))
if(typ==1):
    type="Savings"
elif(typ==2):
    type="Current"
else:
    type="Zero"

obj=BankAcnt(acntnum,name,type)
print(obj.acntdetails(acntnum,name,obj.balance))
c=1
while c==1:
 print("\nselect option:")
 ch=int(input("\n1.Withdraw\n2.Deposite\n3.Account details\n4.Check balance\n5.exit"))
 
 
 if(ch==1):
     amount=float(input("\nEnter the amount to be withdrwan:"))
     obj.withdraw(amount)
 elif(ch==2):
     amount=float(input("\nEnter the amount to deposite:"))
     obj.deposite(amount)
 elif(ch==3):
     print(obj.acntdetails(acntnum,name,type))
 elif(ch==4):
     print(obj.balance)
 else:
     print("thank you")
     c=0
 
        
        

