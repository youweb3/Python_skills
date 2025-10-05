import json  #To save and read data in the JSON format
import os    #To create the correct path between folders (on all systems)

# ------------------- Setup file paths -------------------
# Get the directory of the current script (recipe_manager.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define data folder path relative to this script
DATA_FOLDER = os.path.join(BASE_DIR, "data" )  #The name of the folder where the data is stored.
FILE_PATH = os.path.join(DATA_FOLDER, "recipes.json")   #The full path to the json file

# ------------------- Load function -------------------

def load_recipes (): # Don't need to pass 'recipes' argument to the function, it will read recipes from the JSON file
    if not os.path.exists(FILE_PATH):
        return []  # If file doesn't exist, return empty list
    with open(FILE_PATH, "r", encoding="utf-8") as file:
     return json.load(file) # Read and return data from JSON file

# ------------------- Save function -------------------

def save_recipes(recipes):
    # Make sure the data folder exists
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    
    # write recipes to the Json file
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(recipes, file, ensure_ascii=False, indent=4)
    print("Recipes saved successfully!")

# ------------------- Core functions -------------------

def add_new_recipe(recipes, title, ingredients, instructions):
     # Validation: title and instructions cannot be empty
    if not title.strip() or not instructions.strip():
        print("Title and instructions cannot be empty!")
        return
    
    if not ingredients or all(not i.strip() for i in ingredients):
        print("Ingredients cannot be empty!")
        return
    
    # Create a new recipe dictionary and add it to the recipes list
    recipe = {
        "title": title.strip(),
        "ingredients": [i.strip() for i in ingredients], 
        "instructions": instructions
    }

    recipes.append(recipe)
    print(f"Recipe '{title}' added successfully!")


# # Initialize recipes list outside the function
# recipes = []


def view_recipes(recipes):
    # Display all recipes in the list

    if not recipes:
        print("No recipes available")
        return
    for i, recipe in enumerate(recipes, start=1):  # use enumerate for numbering
        print(f"{i}. {recipe['title']}")
        print("  Ingredients:", ", ".join(recipe["ingredients"]))
        print("  Instructions:", recipe["instructions"])
        print("-" * 45)


def search_recipes(recipes, keyword):
    # Search for recipes by title containing the keyword
    found = []
    for recipe in recipes:
        if keyword.lower() in recipe["title"].lower():
            found.append(recipe)
    return found


def edit_recipe(recipes, index, new_title=None, new_ingredients=None, new_instructions=None):
    # Edit an existing recipe at a given index in the list start from 0
    if index < 0 or index >= len(recipes):
        print("Invalid recipe index.")
        return
    if new_title:
        recipes[index]["title"] = new_title
    if new_ingredients:
        recipes[index]["ingredients"] = new_ingredients
    if new_instructions:
        recipes[index]["instructions"] = new_instructions
    print(f"Recipe '{recipes[index]['title']}' updated successfully!")


def delete_recipe(recipes, index):
    # Delete a recipe at a given index from the list
    if index < 0 or index >= len(recipes):
        print("Invalid recipe index.")
        return
    removed = recipes.pop(index)  # remove recipe by index. With pop we remove the recipe from the list and display its name.
    print(f"Recipe '{removed['title']}' deleted successfully!") 

# ------------------- Load existing recipes -------------------

recipes = load_recipes()  # Read recipes from JSON file

# -------------------  CLI Functions  -------------------
def main_menu():
    # Display the main menu and return user's choice.
    print("====Recipe Manager====")
    print("1. Add a new recipe")
    print("2. View all recipes")
    print("3. Search recipes by title")
    print("4. Edit a recipe")
    print("5. Delete a recipe")
    print("6. Exit and save")
    return input("Enter your choice (1-6):")

# ------------------- CLI Loop -------------------
while True:
    choice = main_menu()

 # --- Choice 1: Add a new recipe ----
    if choice == "1":
        title = input("Enter recipe title: ")
        ingredients = input("Enter ingredients (comma separated): ").split(",")
        ingredients = [i.strip() for i in ingredients]
        instructions= input("Enter instructions: ")
        add_new_recipe(recipes, title, ingredients, instructions)
        save_recipes(recipes)

 # --- Choice 2: View all recipes ---
    elif choice == "2":
        view_recipes(recipes)

 # --- Choice 3: Search recipes by title -----
    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        result = search_recipes(recipes, keyword)
        view_recipes(result)

 # -------- Choice 4: Edit a recipe -----
    elif choice == "4":
        view_recipes(recipes) # Show current recipes so the user can see the index numbers
        try:
             # Ask which recipe to edit (1-based index)
            index = int(input("Enter recipe number to edit: ")) -1
            
            # Validate index to make sure it exists
            if index < 0 or index >= len (recipes):
               print("❌ Invalid recipe number")
               continue
            # Ask for new title (user can skip by pressing Enter)
            new_title = input("Enter new title OR (press Enter to skip): ").strip()
            if new_title == "":
                new_title = None #If empty, keep the old one

            # Ask for new ingredients (comma-separated)
            new_ingredients = input("New ingredients (comma-separated) Or press Enter to skip): ").strip()
            if new_ingredients:
              # Convert string to list and remove extra spaces
              new_ingredients = [i.strip() for i in new_ingredients.split(",")]
            else:
              new_ingredients = None # Keep the old ingredients

            # Ask for new instructions  (optional) OR Enter to skip
            new_instructions = input("Enter new instructions (or press Enter to keep current):")
            if not new_instructions == "": 
               new_instructions = None # Keep the old instructions
            
            # Apply All edits safely
            edit_recipe(recipes, index, new_title or None, new_ingredients, new_instructions)
        
            # Save the updated data to file immediately
            save_recipes(recipes)

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    
     # ------------------- Choice 5: Delete a recipe -------------------
    elif choice == "5":
        view_recipes(recipes)  # Show all recipes so user knows the numbers
        
        # Ask which recipe to delete (convert to list index)
        try:
            index = int(input("Enter recipe number to delete: ")) -1

            #validate he index (make sure it exists)
            if index < 0 or index > len(recipes):
              print("Invalid recipe index.")
              continue # Go back to the menu safely

            #Confirm before deleting
            confirm = input(f"Are you sure you want to delet '{recipes[index]['title']}'? (Y/N):").lower()
            if confirm != "y":
              print("Deletion cancelled.")
              continue #Go back to the menu without deleting

            # Remove the selected recipe
            delete_recipe(recipes, index)

            # Save changes to the file immediately
            save_recipes(recipes)

        except ValueError:
          # Handle invalid (non-numeric) input
          print("Invalid input. please enter a number.")

    # ------------------- Choice 6: Exit and save -------------------
    elif choice == "6":
        # Save all recipes to the JSON file
        save_recipes(recipes)
        print("Exiting Recipe Manager. Goodbye!")
        break

    # --------------- Invalid choice ---------------
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 6.")