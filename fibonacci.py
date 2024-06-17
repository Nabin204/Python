a=0
b=1
c=0
num=int(input("Enter the number of terms:"))
if(num<=0):
 print("Your input is invalid.The number should be greater than 0.")
elif(num==1):
 print(a)
else:
 while(num!=0):
   print(c)
   a=b
   b=c
   c=a+b
   num=num-1
  

 