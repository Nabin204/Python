import math
p=0
def f(x):
    return x**2+5*x+2
def g(x):
    return 2*x+5
a=float(input("Enter initial guess:"))
e=float(input("Enter error:"))
while(abs(f(a)>=e)):
    a=a-f(a)/g(a)
    p=p+1
    print(f"At iteration {p},x={a}")
print("The value of x=",a)
