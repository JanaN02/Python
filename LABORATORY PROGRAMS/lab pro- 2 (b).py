n=int(input("Enter number of elements in list : "))
a=list()

for i in range(0,n):
    b=int(input("Enter the value : "))
    a.append(b)
print("Original list : ",a)

c=int(input("Enter the element to be found : "))

d=len(a)-a.index(c)
print("Positive index : ",a.index(c))
print("Negative index : -",d)