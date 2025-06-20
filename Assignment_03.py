# Assignment_03


# Task 1: Calculate Factorial Using a Function
def factorial(n):
    # Calculate factorial of a number using a loop.
    if n < 2:
        return 1
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


sample_number = 5
print(f"Factorial of {sample_number} is {factorial(sample_number)}")


# Task 2: Using the Math Module for Calculations
import math

number = int(input("Enter a number: "))

# Square root of the number
print(f"Square root of the {number} is", math.sqrt(number))

# Natural logarithm (log base e) of the number
print(f"Natural logarithm of the {number} is", math.log(number))

# Sine of the number (in radians)
print(f"sine of the {number} is", math.sin(number))
