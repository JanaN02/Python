na=input("Enter Your Name : ")
gen=input("Enter Your Gender (M/F) : ")
ag=int(input("Enter Your Age : "))
day=int(input("Enter Your Total Number Of Working Days : "))

if (ag>=18 and ag<30 and gen=='M'):
    x=day*700
    print("The Wage = ",x)
elif (ag>=18 and ag<30 and gen=='F'):
    x=day*750
    print("The Wage = ",x)
elif (ag>=30 and ag<=40 and gen=='M'):
    x=day*800
    print("The Wage = ",x)
elif (ag>=30 and ag<=40 and gen=='F'):
    x=day*800
    print("The Wage = ",x)
else:
    print("Not found")