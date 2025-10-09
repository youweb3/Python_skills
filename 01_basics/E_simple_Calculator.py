num1 = float(input("Enter firsr number: "))
num2 = float(input("Enter secount number: "))
operator = input("Enter operator (+,-,*, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:" , num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operator")