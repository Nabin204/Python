import random
a=int(input("Enter first number for the range:"))
b=int(input("Enter second number for the range:"))
m=random.randrange(a,b)
while(True):
    n=int(input("Enter a number."))
    if(n==m):
        print("The number you entered matches with the random number generated.")
        print(f"Thus the random number is {n}")
        exit(0)
    elif(m>n):
        print("The random number is greater than the number you entered.")
    else:
        print("The random number is smaller than the number you entered.")
       