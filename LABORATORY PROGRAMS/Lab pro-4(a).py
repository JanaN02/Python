def str1(n):
    a=" "
    for i in n:
        a=a+i
    return a

x=int(input("Enter number of elements in tuple : "))
y=list()
for i in range(0,x):
    b=input("Enter the string : ")
    y.append(b)

print("The tuple is : ",tuple(y))
c=tuple(y)
print("The string is : ",str1(c))
