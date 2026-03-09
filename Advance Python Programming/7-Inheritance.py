#1.
# Write a Python program to show single inheritance. 

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

# Derived class (inherits from Person)
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)  # Call base class constructor
        self.roll_no = roll_no

    def display_info(self):
        self.display_name()   # Access parent method
        print("Roll Number:", self.roll_no)

# Create object of Student
s1 = Student("Sakshi", 101)
s1.display_info()


# 2.
# Write a Python program to show multilevel inheritance.

# Base class
class GrandParent:
    def show_grandparent(self):
        print("This is the Grandparent class")

# Derived from GrandParent
class Parent(GrandParent):
    def show_parent(self):
        print("This is the Parent class")

# Derived from Parent
class Child(Parent):
    def show_child(self):
        print("This is the Child class")

# Create object of Child
c1 = Child()
c1.show_grandparent()  # from GrandParent
c1.show_parent()       # from Parent
c1.show_child()        # from Child


#3.
#Write a Python program to show multiple inheritance. 

# First parent class
class Teacher:
    def show_teacher(self):
        print("I am a Teacher.")

# Second parent class
class Researcher:
    def show_researcher(self):
        print("I am a Researcher.")

# Child class (inherits from both Teacher and Researcher)
class Professor(Teacher, Researcher):
    def show_professor(self):
        print("I am a Professor (Teacher + Researcher).")

# Create object of Professor
p1 = Professor()
p1.show_teacher()      # From Teacher
p1.show_researcher()   # From Researcher
p1.show_professor()    # From Professor


#4.
#Write a Python program to show hierarchical inheritance.

# Parent class
class Vehicle:
    def info(self):
        print("This is a vehicle.")

# Child class 1
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

# Child class 2
class Bike(Vehicle):
    def bike_info(self):
        print("This is a bike.")

# Child class 3
class Truck(Vehicle):
    def truck_info(self):
        print("This is a truck.")


# Creating objects of child classes
car = Car()
bike = Bike()
truck = Truck()

print("Car object:")
car.info()
car.car_info()

print("\nBike object:")
bike.info()
bike.bike_info()

print("\nTruck object:")
truck.info()
truck.truck_info()

#5.
# Write a Python program to show hybrid inheritance.
# Parent class
class Person:
    def info(self):
        print("I am a person.")

# Child class 1 (Single Inheritance)
class Student(Person):
    def student_info(self):
        print("I am a student.")

# Child class 2 (Hierarchical Inheritance)
class Teacher(Person):
    def teacher_info(self):
        print("I am a teacher.")

# Another child class inheriting from two classes (Multiple Inheritance)
class TeachingAssistant(Student, Teacher):
    def assistant_info(self):
        print("I am a teaching assistant.")


# Creating objects
s = Student()
t = Teacher()
ta = TeachingAssistant()

print("Student object:")
s.info()
s.student_info()

print("\nTeacher object:")
t.info()
t.teacher_info()

print("\nTeaching Assistant object:")
ta.info()          # From Person
ta.student_info()  # From Student
ta.teacher_info()  # From Teacher
ta.assistant_info()


#6.
# Write a Python program to demonstrate the use of super() in inheritance.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal initialized: {self.name}")

    def sound(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent class constructor using super()
        super().__init__(name)
        self.breed = breed
        print(f"Dog initialized: {self.breed}")

    def sound(self):
        # Call parent method using super()
        super().sound()
        print(f"{self.name} barks.")

# Create object
dog1 = Dog("Tommy", "Labrador")

# Call method
dog1.sound()