#Program11

a=int(input("Enter your salary amount : "))
b=int(input("Enter your year of service : "))

if(b>=10):
    x=a*(10/100)
    y=a+x
    print("10% bonus for the employe")
    print("The bounus amount is : ",y) 
elif(b>=6 and b<10):
    x=a*(8/100)
    y=a+x
    print("8% bonus for the employe")
    print("The bounus amount is : ",y)
elif(b<=5):
    x=a*(5/100)
    y=a+x
    print("The bounus amount is : ",y) 
else:
    print("Sorry, You didn't get bonus")
