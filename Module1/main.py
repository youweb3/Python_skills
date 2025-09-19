print ('Hello, World!')

def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3)) # 8
print(add_numbers(10, -2)) # 8
print(add_numbers(0, 7)) # 7

# ///////////

def subtract_numbers(a, b):
    return a -b
print(subtract_numbers(10,5)) # 5
print(subtract_numbers(5,10)) # -5
print(subtract_numbers(0,0)) # 0

# ////////////

def multiply_numbers(a, b):
    return a * b
print(multiply_numbers(4, 5)) # 20
print(multiply_numbers(-2, 3)) # -6
print(multiply_numbers(0, 100)) # 0

# ////////////

def divide_numbers(a,b):
    if a == 0 and b == 0:
        return 'both numbers are zero'
    elif b == 0:
        return 'Error: Division by zero'
    return a / b
print(divide_numbers(10, 2)) # 5.0
print(divide_numbers(0,0))  # both numbers are zero
print(divide_numbers(5,0))  # Error: Division by zero
print(divide_numbers(0,5)) # 0.0
print(divide_numbers(7, -1)) # -7.0

#////////////////////////

def power_num(a,b):
    return a ** b
print(power_num(2,3)) # 8
print(power_num(5,0)) # 1   

#////////////////////////
def modulus_num(a,b):
    return a % b
print(modulus_num(10,3)) # 1
print(modulus_num(10,2)) # 0

#////////////////////////
def floor_division(a,b):
    return a // b   
print(floor_division(10,3)) # 3
print(floor_division(10,2)) # 5
print(floor_division(10,0)) # Error: Division by zero
print(floor_division(10,-3)) # -4
print(floor_division(10,-5)) # -2

#////////////////////////
import math #library for mathematical functions such as square root, trigonometric functions, logarithms,since,cosine,tangent etc.
def square_root(a):# function to calculate second root of a number
    if a < 0: # check if the number is negative
        return 'Error: Cannot compute square root of a negative number'
    return math.sqrt(a)
print(square_root(16)) # 4.0
print(square_root(0)) # 0.0 
print(square_root(-4)) # Error: Cannot compute square root of a negative number
print(square_root(2)) # 1.4142135623730951
print(square_root(25)) # 5.0
