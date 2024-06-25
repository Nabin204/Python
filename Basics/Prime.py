a=int(input("Enter first number for range:"))
b=int(input("Enter last number for range:"))
count=0
for i in range (a,b+1,1): 
   p=0
   for j in range (2,int(i/2)+1,1):
    if(i%j==0):
     p=p+1
   if(p==0 and i!=1):
       count=count+1
       print(i,end="  ")
print(f"\nThere are {count} prime numbers in between {a} and {b}.")