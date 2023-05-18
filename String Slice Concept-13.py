#String Slice Concept Example Program

a=input("Enter your string : ")
b=int(input("Enter start value : "))
c=int(input("Enter end value : "))
d=int(input("Enter step value : "))

x=a[b:c]
print(x)
y=a[b:c:d]
print(y)
z=a[:c]
print(z)
print(a[b:])


