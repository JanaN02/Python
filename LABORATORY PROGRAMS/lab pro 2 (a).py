a=int(input("Enter number elements in list : "))

I=list()
for i in range(0,a):
    b=int(input("Enter the value : "))
    I.append(b)
print("Original list : ",I)
b=0
c=I[:]
c.sort()

if (c==I):
    b=1

if (b):
    print("Yes, the list is in assending order")
else:
    print("No, the list is not in assening order")