import math
n=int(input("Enter a decimal number:"))
# 1)first method
# m=bin(n).replace("0b","")
# print("The decimal number {} is equivalent to {} binary.".format(n,m))
# 2)Second Method
a=[]
p=""
m=n
while(n!=0):
    a.append(n%2)
    n=n//2
for i in range(len(a)-1,-1,-1):
    p=p+str(a[i])
p=int(p)
print("The decimal number {} is equivalent to {} in binary.".format(m,p))