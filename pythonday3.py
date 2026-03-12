#function in python
def greet():   #defining a function
   print("Hello, Jagriti") #function body or implementation
#greet()  # calling the function


def test(name):  #function with parameter (name is the parameter)
   print("Hello, " + name)


test("Jagriti")  # calling the function with argument


def add(a, b):  #function with parameters a and b
   return a + b  #returning the sum of a and b    
result = add(5, 3)  # calling the function with arguments and storing the result
print("The sum is:", result)  # printing the result