import math
a=int(input("Enter first number for the range:"))
b=int(input("Enter second number for the range:"))
for i in range (a,b,1):
    n=i
    p=0
    c=int(math.log10(n))+1
    while(n!=0):
        r=n%10
        p=p+pow(r,c)
        n=n//10
    if(p==i):
        print(i,end="  ")
