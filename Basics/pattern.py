# 1st pattern
print("First Pattern:")
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()
print()
    
# 2nd pattern
print("Second Pattern:")
for i in range(1,6):
    for j in range(i,6):
        print(i,end=" ")
    print()
print()    

# 3rd pattern
print("Third Pattern")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()    

# 4th pattern
print("Fourth Pattern:")
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()   
 
# 5th pattern
print("Fifth Pattern:")
p=1
for i in range(1,6):
    for j in range(1,i+1):
        print(p,end=" ")
        p += 1
    print()
print()    

# 6th pattern
print("Sixth Pattern:")
q=1
for i in range(1,6):
    for j in range(i,6):
        print(q,end="   ")
        q += 1
    print()
print()    

# 7th pattern
print("Seventh Pattern:")
for i in range(1,6):
    for j in range(1,i+1):
        p -= 1
        print(p,end="   ")
    print()
print()    

# 8th pattern
print("Eighth Pattern:")
for i in range(1,6):
    for j in range(i,6):
        q -= 1
        print(q,end="   ")
    print()
print()    
