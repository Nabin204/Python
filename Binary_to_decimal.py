import math
n=int(input("Enter a binary number:"))
m=n
p=0
c=0
t=0
while(n!=0):
    r=n%10
    if(r!=1 and r!=0):
        t=t+1
    p=p+r*pow(2,c)
    c=c+1
    n=n//10
if(t==0):
    print("The decimal equivalent to binary number is {}".format(p))
else:
    print("Invalid binary number.")