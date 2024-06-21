import math
p=0
a=float(input("Enter first guess:"))
b=float(input("Enter second guess:"))
e=float(input("Enter maximum permissible error:"))
def f(x):
    return 3*pow(x,3)-x-1
c=(a*f(b)-b*f(a))/(f(b)-f(a))
while(abs(f(c))>=e):
    p=p+1
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    a=b
    b=c
    print(f"At iteration {p},x={c}")
print("The value of x is ",c)