a=input("Enter your email : ")

b=a.split("@")[0]
print("Username : ",b)
c=b[::-1].upper()
print("Password : ",b+c)