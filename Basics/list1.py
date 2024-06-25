import random
name=["Nabin","Sumit","Sujan","Dhiraj","Subesh","Pankaj","Alok","Anish"]
print("Before suffling,the list is:")
print(name)
print(random.choice(name))
random.shuffle(name)
print("After suffling,the list is:")
print(name)
#traversing
for i in name:
    print(i)
for i in range(0,len(name),1):
    print(name[i])
