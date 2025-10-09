# Practice basic math functions in Python

# function to add two number
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3)) #8
print(add_numbers(10, -2)) #8
print(add_numbers(0 , 7)) #7

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

print(subtract_numbers(10, 5))  # 5
print(subtract_numbers(5, 10))  # -5
print(subtract_numbers(0, 0))   # 0



# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(4, 5))    # 20
print(multiply_numbers(-2, 3))   # -6
print(multiply_numbers(0, 100))  # 0


# Function to divide two numbers with zero-check
def divide_numbers(a, b):
    if b == 0:
        if a == 0:
            return "Both number are zero"
        return "Error: Division by zero"
    return a / b
print(divide_numbers(10, 2))  # 5.0
print(divide_numbers(0, 0))   # Both numbers are zero
print(divide_numbers(5, 0))   # Error: Division by zero
print(divide_numbers(0, 5))   # 0.0
print(divide_numbers(7, -1))  # -7.0


# Function to calculate power
def power_num(a, b):
    return a ** b

print(power_num(2, 3))  # 8
print(power_num(5, 0))  # 1


# Function to calculate modulus (remainder)
def modulus_num(a, b):
    return a % b

print(modulus_num(10, 3))  # 1
print(modulus_num(10, 2))  # 0


# Function for floor division with zero-check
def floor_division(a, b):
    if b == 0:
        return 'Error: Division by zero'
    return a // b  # The '//' operator divides two numbers and rounds the result down to the nearest integer

print(floor_division(10, 3))   # 3
print(floor_division(10, 2))   # 5
print(floor_division(10, 0))   # Error: Division by zero
print(floor_division(10, -3))  # -4
print(floor_division(10, -5))  # -2