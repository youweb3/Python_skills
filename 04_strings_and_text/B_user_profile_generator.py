firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
age = input("Enter your age:")
city = input("Enter your city:")
occupation = input("Enter your occupation:")

full_name = firstName + " " + lastName
print(full_name)

userDetails = "\"Profile Information:\"\nFull Name: \"{}\"\nThe user is {} years old,\nlives in {},\nand work as a {}.".format(full_name.title(),age,city.title(), occupation.title())

print("\n" + "="*40)
print(userDetails)

print("\n=== UPPERCASE ===")
print(userDetails.upper())

print("\n=== lowercase ===")
print(userDetails.lower())

print("\n=== Capitalize ===")
print(userDetails.capitalize())