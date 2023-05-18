#Write a program to display the multiplication table as below with a given range

a=int(input("Enter start multiplication table : "))
b=int(input("Enter end multiplication table : "))

for i in range(a,b+1):
    for j in range(1,11):
        x=j*i
        print(j,"*",i,"=",x)