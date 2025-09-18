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
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b    
print(divide_numbers(10, 2)) # 5.0
print(divide_numbers(5, 0))  #returns error message
print(divide_numbers(9, 3))  # 3.0
print(divide_numbers(7, -1)) # -7.0
print(divide_numbers(0, 5))  # 0.0

def divide_numbs(a,b):
    if a == 0 and b == 0:
        return 'both numbers are zero'
    elif b == 0:
        return 'Error: Division by zero'
    return a / b
print(divide_numbs(0,0))  # both numbers are zero
print(divide_numbs(5,0))  # Error: Division by zero
print(divide_numbs(0,5)) # 0.0