# 1. Practical Example 5: Write a Python program to find greater and less than a number using if_else

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")


#  2.Write a Python program to check if a number is prime using if_else.


for j in range(3,101) :

    num = 5
    flag = 0

    for i in range(2,num):
        if num%i==0:
            flag=1
            break

    if flag==0:
        print(f"{num} is prime")
    else : 
        pass
        # print(f"{num} is not prime")

    
#  3. Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

# Input the percentage of marks
percentage = float(input("Enter your percentage: "))

# Determine the grade using if-else ladder
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Output the grade
print(f"Your grade is: {grade}")

#  4. Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

# Input: Age and Weight
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

# Checking eligibility
if age >= 18:
    if age <= 65:
        if weight >= 50:
            print("You are eligible to donate blood.")
        else:
            print("You are not eligible to donate blood because your weight is less than 50 kg.")
    else:
        print("You are not eligible to donate blood because your age is above 65.")
else:
    print("You are not eligible to donate blood because your age is below 18.")