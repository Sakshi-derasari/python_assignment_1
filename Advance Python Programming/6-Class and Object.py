#1.
#Write a Python program to create a class and access the properties of the class using an object.

# Define a class
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

# Create an object of Student class
student1 = Student("Sakshi", 101, 92)

# Access properties using object
print("Accessing properties directly:")
print("Name:", student1.name)
print("Roll No:", student1.roll_no)
print("Marks:", student1.marks)

print("\nAccessing properties using method:")
student1.display_info()

#2.
# Write a Python program to demonstrate the use of local and global variables in a class.

# Global variable
message = "I am a GLOBAL variable"

class Demo:
    def __init__(self, value):
        # Instance variable (specific to object)
        self.value = value

    def show_variables(self):
        # Local variable (exists only inside this method)
        local_var = "I am a LOCAL variable"

        print("Accessing global variable inside class:", message)
        print("Accessing instance variable:", self.value)
        print("Accessing local variable:", local_var)

# Create an object
obj = Demo(100)

# Call method
obj.show_variables()

print("\nAccessing global variable outside class:", message)

