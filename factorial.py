num=int(input("enter the number:"))
fact=1
if num==0:
    fact=1
elif num==1:
    fact=1
else:
    for i in range(1,num+1):
        fact=fact*i
print("factorial is:",fact)
