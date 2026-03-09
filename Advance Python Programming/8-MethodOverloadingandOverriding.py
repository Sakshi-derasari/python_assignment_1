#1.
# Write a Python program to show method overloading.

class MathOperations:
    # Method with default and variable arguments to simulate overloading
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0

# Create object
math = MathOperations()

print("Add two numbers:", math.add(10, 20))
print("Add three numbers:", math.add(10, 20, 30))
print("Add one number:", math.add(5))
print("No argument:", math.add())


#2.
# Write a Python program to show method overriding.
# Parent class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Child class
class Dog(Animal):
    # Overriding the parent class method
    def sound(self):
        print("Dog barks.")

# Another Child class
class Cat(Animal):
    # Overriding the parent class method
    def sound(self):
        print("Cat meows.")


# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

print("Parent class method:")
animal.sound()

print("\nOverridden methods in child classes:")
dog.sound()
cat.sound()
