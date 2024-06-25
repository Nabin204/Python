# First Method
lst1=['1','-7','4','78','64','61','50','47']
intlst1=[int(i) for i in lst1]
print(intlst1)

# Second Method
lst2=['1','-7','4','78-32','64//2','61','50','47-8']
intlst2=[eval(i) for i in lst2]
print(intlst2)

#Third Method
intlst3=list(map(int,lst1))
print(intlst3)