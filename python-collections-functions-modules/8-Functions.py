#19.

# Define the function
def print_message():
    message = "Hello, welcome to Python programming!"
    print(message)

# Call the function
print_message()

#20.

# Define the function
def print_sum(a, b):
    result = a + b
    print("The sum of", a, "and", b, "is:", result)

# Call the function with example arguments
print_sum(10, 5)

#21.

# Define the lambda function to square a number
square = lambda x: x * x

# Use the lambda function
num = 5
result = square(num)

# Print the result
print("The square of", num, "is:", result)

#22.

# Lambda function that adds two numbers and multiplies the sum by 2
double_sum = lambda x, y: (x + y) * 2

# Use the lambda function
a = 4
b = 5
result = double_sum(a, b)

# Print the result
print("Result of (a + b) * 2 is:", result)