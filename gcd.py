x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))

for i in range(1,x//2+1):
    if x%i==0 and y%i==0:
        gcd = i
        
print("GCD :",gcd)