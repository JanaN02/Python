def num(n):
    if n<=0:
        print("Invalid")
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return(num(n-1)+num(n-2))

n=int(input("Enter Nth value : "))
print(num(n))