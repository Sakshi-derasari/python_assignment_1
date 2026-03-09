#1.
#Write a Python program to search for a word in a string using re.search().

import re

# Input string
text = "Python is a powerful programming language."

# Word to search
word = "powerful"

# Use re.search()
match = re.search(word, text)

if match:
    print(f"Word '{word}' found at position:", match.start())
else:
    print(f"Word '{word}' not found in the string.")


#2.
#import re

# Input string
text = "Python is a powerful programming language."

# Word to match (at the beginning only)
word = "Python"

# Use re.match()
match = re.match(word, text)

if match:
    print(f"Word '{word}' matched at the beginning of the string.")
else:
    print(f"Word '{word}' not found at the beginning of the string.")