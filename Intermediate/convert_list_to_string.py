# First Method
lst1=["My","Name","is","Nabin","Bhat"]
str1=""
for i in lst1:
    str1 += i+" "
str1=str1[:-1]
print(str1)
print(len(str1))

# Second Method
str2=" "
str2=str2.join(lst1)
print(str2)
print(len(str2))

#Third Method
str3=" ".join(map(str,lst1))
print(str3)
print(len(str3))