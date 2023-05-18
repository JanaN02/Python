
a=int(input("Enter the number : "))
c=a%2
temp=a
rev=0
if(c==0):
    print("Even number and")
    while(a > 0):  
     b= a % 10  
     rev = rev * 10 + b 
     a = a // 10  
    if(temp == rev):  
        print("This number is a palindrome number")  
    else:  
        print("This number is not a palindrome number!")  
else:
    print("Its odd no")

    fact = 1
 
    for i in range(1, a+1):
      fact = fact * i
 
    print("The factorial of",a,"is: ", end="")
    print(fact)
    
    count = 0

    while fact != 0:
     fact //= 10
     count += 1

    print("Number of digits in factorial number: " + str(count))