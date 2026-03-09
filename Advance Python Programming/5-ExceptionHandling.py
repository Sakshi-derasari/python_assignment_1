#1.
#Write a Python program to handle exceptions in a calculator.

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator entered!")

        print("Result:", result)

    except ValueError as ve:
        print("Value Error:", ve)
    except ZeroDivisionError as zde:
        print("Math Error:", zde)
    except Exception as e:
        print("Unexpected Error:", e)

# Run calculator
calculator()

#2.
#Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

def multiple_exceptions_demo():
    try:
        # Try opening a file
        filename = input("Enter file name: ")
        with open(filename, "r") as f:
            data = f.read()
            print("\nFile contents:\n", data)

        # Division example
        num1 = int(input("\nEnter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
        print("Division result:", result)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("\nNo exceptions occurred. Program executed successfully!")
    finally:
        print("Program execution completed.")

# Run the demo
multiple_exceptions_demo()

#3.
# Write a Python program to handle file exceptions and use the finally block for closing the file. 
def read_file():
    file = None
    try:
        filename = input("Enter file name: ")
        file = open(filename, "r")   # may raise FileNotFoundError
        content = file.read()
        print("\nFile contents:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        if file:
            file.close()
            print("File closed successfully (finally block executed).")

# Run the function
read_file()

#4.
#Write a Python program to print custom exceptions.
# Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed!"):
        super().__init__(message)

# Another custom exception
class TooLargeNumberError(Exception):
    def __init__(self, message="Number is too large!"):
        super().__init__(message)

def check_number(num):
    try:
        if num < 0:
            raise NegativeNumberError("You entered a negative number.")
        elif num > 1000:
            raise TooLargeNumberError("The number exceeds the limit (1000).")
        else:
            print(f"Valid number: {num}")
    except (NegativeNumberError, TooLargeNumberError) as e:
        print("Custom Exception:", e)

# Example usage
n = int(input("Enter a number: "))
check_number(n)