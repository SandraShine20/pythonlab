n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number:"))
print("1.Additon\n2.Substraction\n3.Multiplication\n4.division")
ch=int(input("enter the choice"))
if ch==1:
    print(n1+n2)
elif ch==2:
    print(n1-n2)
elif ch==3:
    print(n1*n2)
elif ch==4:
    print(n1/n2)
else:
    print("invalid choice")
    
