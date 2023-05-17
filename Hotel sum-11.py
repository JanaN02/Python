print("1,Bad \n 2,Notbad \n 3,Average \n 4,Good \n 5,Excellent")

a=int(input("Enter your food rating (1-5): "))
b=int(input("Enter your Service rating (1-5): "))
c=int(input("Enter your ambience rating (1-5): "))
d=int(input("Enter your bill amount (1-5): "))

bad=1
not_bad=2 
average=3
good=4
excellent=5

if a==4 or a==5:
    if b==4 or c==4 or b==5 or c==5:
        tip=d*(10/100)
        print("Tips = ",tip)
    else:
        tip=d*(5/100)
        print("Tips = ",tip)

if a==1 or a==2 or a==3:
    if b==4 or c==4 or b==5 or c==5:
        tip=d*(5/100)
        print("Tips = ",tip)
    else:
        tip=d*(1/100)
        print("Tips = ",tip)
        