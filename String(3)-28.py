
a=input("Enter your string : ")
b=len(a)
if b%5==0:
    print("The length of the string is multiple of 5")
    c=a.upper()
    print(c[::-1])
else:
    print("The length of the string is not multiple of 5")