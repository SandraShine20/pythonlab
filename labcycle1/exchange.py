s=input("enter string:")
li=list(s)
temp=li[0]
li[0]=li[-1]
li[-1]=temp
string = ''
for i in li:
    string+=i
print(string)

