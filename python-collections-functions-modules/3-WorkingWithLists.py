#5.

# Define a sample list
my_list = ["apple", 10, 3.14, True, "banana"]

# Print a message
print("Elements in the list:")

# Iterate through the list and print each element
for element in my_list:
    print(element)


#6.

# Create an empty list
my_list = []

# Use a for loop to insert elements into the list
for i in range(5):  # This will run 5 times (0 to 4)
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

# Print the final list
print("\nFinal list:")
print(my_list)
