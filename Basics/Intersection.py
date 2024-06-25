# INPUT

m=int(input("Enter the number of elements in first set:"))
n=int(input("Enter the number of elements in second set:"))
set1=set()
set2=set()
print("Enter elements of first set:")
for _ in range(m):
    set1.add(int(input()))
print("Enter elements of second set:")
for _ in range(n):
    set2.add(int(input()))

# Method 1

result1=set1.intersection(set2)

# OUTPUT

print("The first set is:",set1)
print("The second set is:",set2)
print("The intersection of these sets is:",result1)
print()

# Method 2

result2=set()
for i in set1:
    if(i in set2):
        result2.add(i)
        
#OUTPUT

print("The intersection of these sets is:",result2)

