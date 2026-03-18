# lambda functions in python
# a function without a  name is anonymous function or lambda function
# used when we need a small function for a short period of time

# syntax: lambda arguments: expression
#normal function

def add(x, y):
    return x + y

print(add(5, 3)) # output: 8

# using lamda function  syntax:lambda arguments: operation
add_lamda = lambda x, y: x+y
print(add_lamda(4,2))

square = lambda x: x**2
print(f"Square of 5 is {square(5)}")


print("################################### lambda function with map(),filter and sorted ###################################")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# from using index
for i, num in enumerate(numbers): # enumerate() function adds a counter to an iterable and returns it as an enumerate object
    print(f"Index: {i}, Number: {num}")

# iterating dictionary
student = {"name": "John", "age":30}
for key, value in student.items(): # items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
    print(f"Key: {key}, Value: {value}")


# sorted() function 
# used to sort the elements of a list in ascending or descending order
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(sorted(numbers)) # sorting in ascending order
print(sorted(numbers, reverse=True)) # sorting in descending order

# sort by key
students = [("John", 25), ("Jane", 22), ("Doe", 30)]
sorted_students = sorted(students, key=lambda x: x[1]) # sorting by age
print(sorted_students)

print("------filter() function------")
# filter () function
# used to filter elements based on a condition
# syntax: filter(function, iterable)
# filter student who passed
students = [{"name":"Rita", "marks":80}
            ,{"name":"Sita", "marks":45}
            ,{"name":"Gita", "marks":60}]

passed_students = filter(lambda x:x["marks"]>=50,students)
print(f"Passed students: {list(passed_students)}")


numbers = [1, 2, 3, 4, 5, 6]

even_numbers= filter(lambda x: x % 2 == 0, numbers) # filtering even numbers
print(list(even_numbers))


# without lambda function
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

print("------map() function------")
# map() function
# used to apply a function to all the elements of an iterable
# syntax: map(function, iterable)
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x:x**2, numbers)) # squaring each number in the list
print(squared_numbers)

# multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = list(map(lambda x,y: x+y, numbers1,numbers2)) # adding corresponding elements of two lists
print(result)


# lambda with multiple conditions
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4)) 

# lambda returning multiple values
calculate = lambda x:(x, x**2, x**3)
print(calculate(5))

# nested lambda function
nested_lamda = lambda x: (lambda y: x +y)
print(nested_lamda(5)(3))
