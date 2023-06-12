def rev(n):
    a=( )
    for j in reversed(n):
        a=a+(j,)
    return a

x=int(input("Enter number element in tuple : "))
y=list()

for i in range(0,x):
    b=input("Enter the string : ")
    y.append(b)

print("The tuple is : ",tuple(y))
c=tuple(y)
print("The revese tuple : ",rev(c))
