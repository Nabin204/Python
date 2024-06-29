str1="Nabin Bhat"
for index,value in enumerate(str1):
    print(f"Index:{index}, value:{value}")
    
lst1 = list(enumerate(str1,1))
print(lst1)

languages = ["Python","C","C++","Javascript","Java"]
for i in enumerate(languages):
    print(i)
    
# Finding next element
enumerate_languages = enumerate(languages)
next_element = next(enumerate_languages)
print(f"Next element : {next_element}")