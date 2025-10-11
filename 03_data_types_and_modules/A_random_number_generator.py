# ==========================================
# Project: Random Number Generator
# Description: Generates a random number between 1 and 100 and displays its type.
# ==========================================

# 1. Import the random module
import random

# 2. Generate a random integer between 1 and 100
random_number = random.randint(1, 100)

# 3. Print the random number and its data type
print("Generated random number:", random_number)
print("Data type:", type(random_number))

# 4. Convert the number to float and complex
FloatNumber = float(random_number)
complex_number = complex(random_number)

# 5. Display the converted values and their types
print("\nType conversions:")
print("As float:", FloatNumber, "| Type:", type(FloatNumber))
print('As comples:', complex_number, '| Type:', type(complex_number))

# 6. End of program
print("\nProgram completed successfully!")
print("-" *45)