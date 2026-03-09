#  1. datatype i have used is integer. 
# variable i have used to take value and store it are a and b.
a =int(input("Enter value of a:"))  
b =int(input("Enter value of b:"))

c =float(a)
print(float(a)+b)

# x = 5           # integer
# name = "Alice"   # string



#  2. Practical Example 1: How does the Python code structure work?

# correct indentation

# if condition:
#     # This block is indented, part of the 'if' statement
#     print("Condition is True")

# correct loop structure
# # for i in range(5):
#     print(i)  # Prints numbers 0 to 4

# or 

# count = 0
# while count < 5:
#     print(count)
#     count += 1  # Increment count


#  3.Practical Example 2: How to create variables in Python?
# basic syntex of variable is :

# variable_name = value

# age = 25  integer variable
# name="sakshi"  string variable
# price = 19.99 float variable 

# there are many other variables like list, boolean, etc.

'''
# rules to create variable.
Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
The first character of a variable name cannot be a digit.
Python is case-sensitive, so name and Name are considered different variables.
Avoid using Python reserved keywords (such as if, else, while, True, False, class, etc.) as variable names.

'''

#  4. Practical Example 3: How to take user input using the input() function.

# Taking user input
def calculator(A, B, choice):
    A = int(input("Enter the value for A: "))
    B = int(input("Enter the value for B: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter choice (1/2/3/4): "))

    result = calculator(A, B, choice)
    print("Result:", result)


#  5. Practical Example 4: How to check the type of a variable dynamically using type().
# synetx is :  type(variable)

# Integer
num = 10
print(type(num))  # <class 'int'>

# String
name = "Alice"
print(type(name))  # <class 'str'>

# Float
price = 19.99
print(type(price))  # <class 'float'> 