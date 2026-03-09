#15.

# sample dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Print original dictionary
print("Original dictionary:", my_dict)

# Update the value at key 'age'
my_dict["age"] = 26

# Update the value at key 'city'
my_dict["city"] = "Los Angeles"

# Print updated dictionary
print("Updated dictionary:", my_dict)


#16.

# sample dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Get all keys
keys = list(my_dict.keys())

# Get all values
values = list(my_dict.values())

# Print keys and values separately
print("Keys:", keys)
print("Values:", values)

#17.

# Sample lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Create an empty dictionary
my_dict = {}

# Use for loop to fill the dictionary
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# Print the resulting dictionary
print("Dictionary created from two lists:")
print(my_dict)

#18.

# Sample string
input_str = "hello world"

# Create an empty dictionary to store character counts
char_count = {}

# Loop through each character in the string
for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character counts
print("Character frequencies:")
for key, value in char_count.items():
    print(f"'{key}': {value}")