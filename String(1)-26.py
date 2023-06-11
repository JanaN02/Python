
s=input("Enter your string : ")

if len(s)<=2:
    print(" ")
else:
    a=s[0:2] + s[-2:]
    print(a)