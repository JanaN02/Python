#program7

x=int(input("Enter birth year : "))
y=int(input("Enter current year : "))

z=y-x
print("Age of customer : ",z)

if z>=60:
  a=1020*(20/100)
  print("The amni bus charge : ",a)
else:
  print("The amni bus charge : 1020")
