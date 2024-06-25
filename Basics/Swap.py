a=int(input("Enter first number:"))
b=int(input("Enter first number:"))
print(f"Before swapping,The value of a is {a} and b is {b}.")

#First Method
c=a
a=b
b=c
print(f"After swapping,The value of a is {a} and b is {b}.")

#Second Method

a,b=b,a
print(f"Again swapping, The value of a is {a} and b is {b}.")
