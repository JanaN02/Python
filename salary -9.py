#Program11

a=int(input("Enter your salary amount : "))
b=int(input("Enter your year of service : "))

if(b>10):
    print("10% bonus for the employe")
elif(b>=6 and b<10):
    print("8% bonus for the employe")
else:
    print("15% bonus for the employe")