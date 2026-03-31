#1. 
# Creating a list with multiple data types
mixed_list = [42, "Hello", 3.14, True, None, [1, 2, 3], {"key": "value"}]

#  list
print("The mixed data type list is:")
print(mixed_list)

# each element with its type
print("\nElements with their data types:")
for element in mixed_list:
    print(f"{element} -> {type(element)}")

#2.

# a sample list
my_list = ["apple", 10, 3.14, True, "banana", 99]

# full list
print("Original List:")
print(my_list)

# Accessing elements using index positions
print("\nAccessing elements at different index positions:")
print("Element at index 0:", my_list[0])     # First element
print("Element at index 2:", my_list[2])     # Third element
print("Element at index -1:", my_list[-1])   # Last element
print("Element at index -3:", my_list[-3])   # Third from lasT