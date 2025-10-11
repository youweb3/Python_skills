# B_math_operations_with_module.py
# This project demonstrates the use of Python's math module and its functions.

# 1. Import the math module
import math

# 2. Define some numbers for demonstration
num1 = 16
num2 = 7
num3 = 3.14

# 3. Basic math operations using math module
square_root_num1 = math.sqrt(num1)        # square root
power_num1_num2 = math.pow(num1, num2)    # num1 raised to the power of num2
ceil_num3 = math.ceil(num3)               # round up
floor_num3 = math.floor(num3)             # round down
factorial_num2 = math.factorial(num2)     # factorial

#4.Print results with explanatins
print("Math module operations: \n")
print(f"square root of {num1} is {square_root_num1}")
print(f"{num1} raised to the power of {num2} is {power_num1_num2}")
print(f"Ceilling of {num3} is {ceil_num3}")
print(f"Floor of {num3} is {floor_num3}")
print(f"Factorial of {num2} is {factorial_num2}")

# 5. End of program
print("\nProgram completed successfully!")
print("-" *45)

#///////////////////////
# This project demonstrates how to convert between different data types in Python.

# 1. Define variables of different types
int_num = 10
float_num = 5.75
str_num = "20"
complex_num = 3 + 4j

# 2. Convert int to float and str
int_to_float = float(int_num)
int_to_str = str(int_num)

# 3. Convert float to int and str
float_to_int = int(float_num)
float_to_str = str(float_num)

# 4. Convert str to int and float
str_to_int = int(str_num)
str_to_float = float(str_num)

# 5. Convert int to complex
int_to_complex = complex(int_num)

# 6. Print all conversions with type
print("Type Conversion Examples:\n")

print(f"{int_num} as float: {int_to_float} ({type(int_to_float)})")
print(f"{int_num} as string: '{int_to_str}' ({type(int_to_str)})")

print(f"{float_num} as int: {float_to_int} ({type(float_to_int)})")
print(f"{float_num} as string: '{float_to_str}' ({type(float_to_str)})")

print(f"'{str_num}' as int: {str_to_int} ({type(str_to_int)})")
print(f"'{str_num}' as float: {str_to_float} ({type(str_to_float)})")

print(f"{int_num} as complex: {int_to_complex} ({type(int_to_complex)})")

print("\nProgram completed successfully!")
