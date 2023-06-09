def sph(pi,r):
    sa=4*pi*r*r
    vol=(4/3)*pi*r*r*r
    print("Surface Area of sphere : ",sa)
    print("Volume of sphere : ",vol)
def cyl(pi,r,h):
    sa=(2*pi*r*r)+(2*pi*r*h)
    vol=pi*r*r*h
    print("Surface Area of cylinder : ",sa)
    print("Volume of cyclinder : ",vol)
def con(pi,r,h,s):
    sa=(pi*r*s)+(pi*r*r) 
    vol=(1/3)*(pi*r*r*h)
    print("Surface Area of cone : ",sa)
    print("Volume of cone : ",vol)
def rec(l,h,w):
    sa=2*(l*w+l*h+w*h)
    vol=l*w*h
    print("Surface Area of Rectangular prism : ",sa)
    print("Volume of Rectangular prism : ",vol)
def tri(b,h,l,s):
    sa=(b*h)+(2*l*s)+(l*b)
    vol=(1/2)*(b*l)*h
    print("Surface Area of Triangular prism : ",sa)
    print("Volume of Triangular prism : ",vol)

print("\n 1,Sphere \n 2,Cylinder \n 3,Cone \n 4,Rectangular Prism \n 5,Triangular Prism")
cho=int(input('\n Enter your choice [1,2,3,4,5] : '))

if(cho==1):
    r=int(input("\n Enter Sphere Radius : "))
    sph(3.14,r)
elif(cho==2):
    r=int(input("\n Enter Sphere Radius : "))
    h=int(input("Enter Sphere Height : "))
    cyl(3.14,r,h)
elif(cho==3):
    r=int(input("\n Enter Cone Radius : "))
    h=int(input("Enter Cone Height : "))
    s=int(input("Enter Cone Slantheight : "))
    con(3.14,r,h,s)
elif(cho==4):
    l=int(input("\n Enter Rectangular Prism Length : "))
    h=int(input("Enter Rectangular Prism Height : "))
    w=int(input("Enter Rectangular Prism Width : "))
    rec(l,h,w)
elif(cho==5):
    b=int(input("\n Enter Rectangular Prism Width : "))
    h=int(input("Enter Rectangular Prism Width : "))
    l=int(input("Enter Rectangular Prism Width : "))
    s=int(input("Enter Rectangular Prism Width : "))
    tri(b,h,l,s)
else:
    print("\n Your Choice is invalid")