str1=input("Enter string 1 : ")
str2=input("Enter string 2 : ")
str3=""
temp=0
len1=len(str1)
len2=len(str2)
for i in range(0,len2):
    for j in range(temp,len1):
        if(str2[i]==str1[j]):
            str3=str3+str1[j]
            temp=j+1
            break
if (str2==str3):
    print("Yes")
else:
    print("no")