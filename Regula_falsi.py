import math
p=0
a=float(input("Enter first guess:"))
b=float(input("Enter second guess:"))
e=float(input("Enter maximum permissible error:"))
def f(x):
    return pow(x,2)+5*x+2
c=(a*f(b)-b*f(a))/(f(b)-f(a))
if(f(a)*f(b)>0):
    print("The initial guess are wrong.")
else:
    while(abs(f(c))>=e):
        p=p+1
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(a)*f(c)<0):
            b=c
        else:
            a=c
        print(f"At iteration {p},x={c}")
