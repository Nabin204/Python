#Traversing in Dictionary

#Method 1
student1 = {
    'Name' : "Nabin Bhat",
    'Age' : 21,
    'Address' : 'Lamachaur, Pokhara',
    'Level' : 'Bachelor',
    'Faculty' : 'BCT',
    'Campus' : "Paschimanchal Campus"
    }
for i in student1:
    print(i)
    print(student1[i])
    print()

#Method 2

for key1,value1 in student1.items():
    print(f"{key1} : {value1}")
print()


#Traversing in nested Dictionary

info = {
    'Student1' : {
    'Name' : "Nabin Bhat",
    'Age' : 21,
    'Address' : 'Lamachaur, Pokhara',
    'Level' : 'Bachelor',
    'Faculty' : 'BCT',
    'Campus' : "Paschimanchal Campus"
    },
    'Student2' : {
    'Name' : "Dhiraj Mahato",
    'Age' : 20,
    'Address' : 'Lamachaur, Pokhara',
    'Level' : 'Bachelor',
    'Faculty' : 'BCT',
    'Campus' : "Paschimanchal Campus"
    },
    'Student3' : {
    'Name' : "Sumit Sah",
    'Age' : 21,
    'Address' : 'Lamachaur, Pokhara',
    'Level' : 'Bachelor',
    'Faculty' : 'BCT',
    'Campus' : "Paschimanchal Campus"
    }
    }

for key1,value1 in info.items():
    print(key1)
    for key2,value2 in value1.items():
        print(f"{key2} : {value2}")
    print()

