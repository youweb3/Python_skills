import math

#=========Functions for basic arithmetic operations========#

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b    

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if a == 0 and b == 0:
        return 'both numbers are zero'
    elif b == 0:
        return 'Error: Division by zero'
    return a / b

def power_numbers(a, b):
    return a ** b

def square_root(a):
    if a < 0: #===square root of negative number is not defined in real numbers
        return 'Error: Cannot compute square root of negative number'
    return math.sqrt(a) 


#=========Main program to take user input and perform operations========#
print("Welcome to the Basic Calculator!")

num1 = float(input("Enter first number: ")) # takes input from user,the input always returns a string which we need to convert to float or int
num2 = float(input("Enter second number ignored for sqrt: "))
operation = input('choose operation ( +, -, *, /, ^, sqrt):').lower()


#=========Perform the operation based on user input========#

if operation == '+':
    result = add_numbers(num1, num2)
elif operation == '-':
    result = subtract_numbers(num1, num2)
elif operation == '*':
    result = multiply_numbers(num1, num2)
elif operation == '/':
    result = divide_numbers(num1, num2)
elif operation == '^':
    result = power_numbers(num1, num2)
elif operation == 'sqrt':
    result = square_root(num1) # only one number is needed for square root
else:
    result = 'Invalid operation'

#=========Display the result========#

print('Result:', result)