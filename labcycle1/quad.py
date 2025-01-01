import math

a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))

if a==0:
    print("no solution")
else:
    d=math.sqrt((b*b)-(4*a*c))
    if d==0:
        sol=-b/(2*a)
        print("one root:",sol)
    elif d<0:
        print("complex roots")
    else:
        sol1=(-b+d)/(2*a)
        sol2=(-b-d)/(2*a)
        print("root 1:",sol1)
        print("root 2:",sol2)
