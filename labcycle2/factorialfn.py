def fact(num):
    if num == 0 or num==1:
        return 1
    else:
        f=num*fact(num-1)
        return f


num=int(input("enter the number:"))
print("factorial:",fact(num))



    

