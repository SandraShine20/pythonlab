s=input("enter string:")
li=[]
for i in range(0,len(s)):
    li.append(s[i])
temp=li[0]
li[0]=li[-1]
li[-1]=temp
string = ''
for i in li:
    string+=i
print(string)

