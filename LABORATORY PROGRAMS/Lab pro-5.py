x=int(input("Enter number elements in a set : "))
y=int(input("Enter number elements in b set : "))

a=list()
b=list()

for i in range(0,x):
    c=int(input("Enter value a set : "))
    a.append(c)

for j in range(0,y):
        d=int(input("Enter value b set : "))
        b.append(d)

d=set(a)
print("a=",d)
e=set(b)
print("b=",e)

print(d.issubset(e))