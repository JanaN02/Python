#Program3

t=float(input("Enter temperature :"))
v=float(input("Enter wind speed :"))

x=13.12+0.6215*t-11.3*v**0.16+0.3965*t*v**0.16

print("Wind chill index : ",x)