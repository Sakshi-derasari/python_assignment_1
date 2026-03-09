# 1. 
# Program to read contents of a file and print them

filename = "example.txt"

try:
    with open(filename, "r") as file:
        contents = file.read()
        print("File Contents:\n")
        print(contents)
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 2. 
# Program to write multiple strings into a file

# specify the filename
filename = "output.txt"

# list of strings to write
strings = [
    "Hello, this is the first line.",
    "Python makes file handling easy.",
    "This is the last line."
]

try:
    with open(filename, "w") as file:
        for line in strings:
            file.write(line + "\n")   # add newline after each string
    print(f"Strings have been written successfully to '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")