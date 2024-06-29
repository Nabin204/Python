def even_check(n : int)->bool:
    if(n%2==0):
        return True
    else:
        return False
numbers = [2,4,1,88,92,34,67,10,78,23,15,67]
even_numbers = list(filter(even_check,numbers))
print(even_numbers)

# Fiter with lambda function
odd_numbers = list(filter(lambda x: x%2 != 0,numbers))
print(odd_numbers)

numbers_betn = list(filter(lambda x : x>10 and x<50,numbers))
print("The numbers between 10 and 50 are:")
print(numbers_betn)