#23.

import math

# Using math.sqrt() to compute square root
num = 16
sqrt_result = math.sqrt(num)
print(f"Square root of {num} is:", sqrt_result)

# Using math.factorial() to compute factorial
n = 5
factorial_result = math.factorial(n)
print(f"Factorial of {n} is:", factorial_result)

# Using math.pow() to compute power
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power {exponent} is:", power_result)

# Using math.pi to get the value of π
print("The value of pi is:", math.pi)

# Using math.sin() to compute sine (angle in radians)
angle = math.pi / 2  # 90 degrees
sine_result = math.sin(angle)
print(f"Sine of 90 degrees (π/2 radians) is:", sine_result)

#24.

import random

# Generate a single random number between 1 and 100
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# If you want to generate multiple random numbers, for example 5 numbers:
print("Five random numbers between 1 and 100:")
for _ in range(5):
    print(random.randint(1, 100))