# 1) Even and odd number checker function
even_odd_check =lambda x: f"{x} is an even number." if x%2==0 else f"{x} is an odd number."
print(even_odd_check(87))
print(even_odd_check(112))

# 2) Arithmetic operation
add = lambda x,y : x+y
subtract = lambda x,y : x-y
multiply = lambda x,y : x*y
divide = lambda x,y : x/y
print(add(23,75))
print(subtract(34,23))
print(multiply(23,75))
print(divide(34,23))

# 3) Filtering a list
numbers = [i for i in range(76)]
even_numbers =  list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

# 4) Mapping a function to a list
lst1=[6,2,9,0,2,5]
squared_numbers = list(map(lambda x: x**2,lst1))
print(squared_numbers)

# 5) Using lambda in key function
fruits = ["Apple","Litchi","Mango","Pineapple","Watermelon","Guava"]
fruits.sort()
print(fruits)
sorted_fruits = sorted(fruits,key = lambda x:len(x))
print(sorted_fruits)

# 6) Creating a simple calculator with lambda function
calculator = {
    "add" : lambda x,y : x+y,
    "subtract" : lambda x,y : x-y,
    "multiply" : lambda x,y : x*y,
    "divide" : lambda x,y : x/y,
}
print(calculator["divide"](9,4))
print(calculator["multiply"](8,9))

# 7) Using lambda in list comprehension
# Passing lambda function as argument
lst2 = [6,9,2,11,4,5]
cube_numbers = [(lambda x : x**3)(x) for x in lst2]
print(cube_numbers)

# 8) Lambda functions in higher order function
def operate_on_numbers(x,y,operation):
    return operation(x,y)
result = operate_on_numbers(12,16,lambda a,b:a/b)
print(result)