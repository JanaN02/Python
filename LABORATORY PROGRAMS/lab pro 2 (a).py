n=int(input("Enter number of elements in list : "))
a=list()

for i in range(0,n):
    b=int(input("Enter the value : "))
    a.append(b)
print("Original list : ",a)

c=int(input("Enter the element to be found : "))

posi=[]
nega=[]
d=len(n)
for i in range(0,d):
    if n[i]==a:
        posi.append(i)
        nega.append(-len(n)+i)
print("Positive index: ",posi)
print("Negative index : ",nega)
