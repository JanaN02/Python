def inter(p,n,r):
    inter=(p*n*r)/100
    print("Interst : ",inter)

name=input("Enter your name : ")
age=int(input("Enter your age  : "))
gen=input("Enter your gender (M/F) : ")
pri_amo=int(input("Enter your princial amount : "))
year=int(input("Enter no of years : "))

if(age>=60):
   r=12
   inter(pri_amo,year,r)
elif(age<60 and gen=="f"):
    r=10
    inter(pri_amo,year,r)
else:
    r=9
    inter(pri_amo,year,r)
