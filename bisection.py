import math
a=float(input("Enter first guess:"))
b=float(input("Enter second guess:"))
E=float(input("Enter the maximum possible error:"))
p=0
def f(num):
    return num**3+5*num+24
if(f(a)*f(b)<0):
  while(abs(a-b)>E):
    c=(a+b)/2
    p=p+1
    print(f"At iteration {p},x={c}")
    if(f(a)*f(c)<0):
        b=c
    else:
        a=c  
else:
    print("The initial guess are wrong.Try again using another guesses.")
    