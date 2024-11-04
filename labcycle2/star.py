a=int(input("enter range:"))
n=2*a+1
temp=1
for i in range(1,n+1):
    if i>(n//2)+1:
        lim = i - temp
        temp+=2
    else:
        lim = i+1  
    for j in range(1,lim):
        print("*" ,end="  ")
    print("")
    



