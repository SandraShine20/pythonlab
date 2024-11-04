s1=input("1st string:")
s2=input("2nd string:")


li1=list(s1)
li2=list(s2)


temp1=li1[0]
temp2=li2[0]

li1[0]=temp2
li2[0]=temp1

li3=li1+li2

s3=""
for i in li3:
    s3+=i

print(s3)
