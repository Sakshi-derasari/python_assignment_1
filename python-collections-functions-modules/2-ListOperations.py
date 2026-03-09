#3.

# empty list
my_list = []

# Adding elements using append()
my_list.append("apple")
my_list.append("banana")
print("After using append():")
print(my_list)

# Adding element at a specific position using insert()
my_list.insert(1, "mango")  # Inserts 'mango' at index 1
print("\nAfter using insert():")
print(my_list)


#4.

# a sample list
fruits = ["apple", "banana", "cherry", "banana", "orange"]

print("Original List:")
print(fruits)

# Removing element by value using remove()
fruits.remove("banana")  # Removes the first occurrence of 'banana'
print("\nAfter using remove('banana'):")
print(fruits)

# Removing element by index using pop()
removed_item = fruits.pop(2)  # Removes the element at index 2
print(f"\nAfter using pop(2), removed: {removed_item}")
print(fruits)
