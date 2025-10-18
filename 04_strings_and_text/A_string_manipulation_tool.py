input_text = input("Enter Some Text:")
print("\n\"Manipulation\"")
print("Option 1: Convert to uppercase:")
print("Option 2: Convert to lowercase")
print("Option 3: Slice the string from a start index to an end index")
print("Option 4: Calculate the length of the string")
print("Option 5: Loop through each character in the string and display it on a new line")

choice =input("choose your Method (1 -5):")
print("\nYou selected:", choice)

if choice == "1":
    result = input_text.upper()
    print("Your text converted to upperCase:" , result)

elif choice == "2":
    result = input_text.lower()
    print("Your text converted to lowerCase" , result)

elif choice == "3":
    start = int(input("Enter stat index:"))
    end = int(input("Enter end index:"))
    result = input_text[start:end]
    print("Your text sliced:" , result)

elif choice == "4":
    result = len(input_text)
    print("Your text length:" , result)

elif choice == "5":
    print("Characters in your text:")
    for char in input_text:
        print(char)
else:
    print("Invalid choice. Please select a number between 1 and 5.")