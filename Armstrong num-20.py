#Armstrong numbers find in given range

x=int(input("Enter your lower number : "))
y=int(input("Enter your upper number : "))

for i in range(x,y+1):
    sum=0
    temp=i
    while temp>0:
        a=temp%10
        sum+=a**3
        temp//=10
        if i==sum:
            print(i)