
# Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']

# Define the list of fruits
list1 = ['apple', 'banana', 'mango']

# Loop through each fruit in the list and print it
for fruit in list1:
    print(fruit)



# Practical Example 2: Write a Python program to find the length of each string in List1.

list1 = ['apple', 'banana', 'mango']

# Loop through each string in the list and find its length
for fruit in list1:
    print(f"The length of '{fruit}' is {len(fruit)}.")



# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

list1 = ['apple', 'banana', 'mango']

# Input the string to search for
search_str = input("Enter the string to search for: ")

# Loop through the list to find the string
found = False
for fruit in list1:
    if fruit == search_str:
        found = True
        break

# condition to display the result  
if found:
    print(f"'{search_str}' is in the list.")
else:
    print(f"'{search_str}' is not in the list.")


# Practical Example 4: Print this pattern using nested for loop:
# * 
# **
# ***
# ****
# *****

for i in range (1,6):
    for j  in range (1,i+1):
        print("*",end="")
    print("")