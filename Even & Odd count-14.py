#Even & Odd count in given range

a=int(input("Enter start value : "))
b=int(input("Enter end value : "))
x=0
y=0
for i in range(a,b+1):
    if(i%2==0):
        x=x+1
    else:
        y=y+1

print("Event count : ",x)
print("Odd count : ",y)