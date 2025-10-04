import json  #To save and read data in the format
import os    #To create the correct path between folders (on all systems)

# Get the directory of the current script (recipe_manager.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define data folder path relative to this script
DATA_FOLDER = os.path.join(BASE_DIR, "data" )  #The name of the folder where the data is stored.
FILE_PATH = os.path.join(DATA_FOLDER, "recipes.json")   #The full path to the recipes.json file inside that folder.

# DATA_FOLDER = "data" 
# #FILE_PATH = os.path.join(DATA_FOLDER, "recipes.json")

def add_new_recipe(recipes, title, ingredients, instructions):
    # Create a new recipe dictionary and add it to the recipes list
    recipe = {"title": title, "ingredients": ingredients, "instructions": instructions}

    recipes.append(recipe)
    print(f"Recipe '{title}' added successfully!")


# Initialize recipes list outside the function
recipes = []

add_new_recipe(
    recipes, "Pasta", ["Pasta", "Tomato", "Cheese"], "Boil pasta, add sauce, serve."
)
add_new_recipe(
    recipes, "Pizza", ["Pasta", "Tomato", "Cheese"], "Boil pasta, add sauce, serve."
)
print(recipes)


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


print("\nViewing all recipes:")
view_recipes(recipes)


def search_recipes(recipes, keyword):
    # Search for recipes by title containing the keyword
    found = []
    for recipe in recipes:
        if keyword.lower() in recipe["title"].lower():
            found.append(recipe)
    return found


# Test the search function
print("\nSearching for 'pasta':")
results = search_recipes(recipes, "pasta")
view_recipes(results)


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

edit_recipe(recipes, 0, new_title="Spaghetti", new_ingredients=["Spaghetti", "Tomato Sauce", "Cheese"], new_instructions="Boil spaghetti, add sauce, serve.")
view_recipes(recipes)


def delete_recipe(recipes, index):
    # Delete a recipe at a given index from the list
    if index < 0 or index >= len(recipes):
        print("Invalid recipe index.")
        return
    
    removed = recipes.pop(index)  # remove recipe by index. With pop we remove the recipe from the list and display its name.
    print(f"Recipe '{removed['title']}' deleted successfully!")

view_recipes(recipes)
delete_recipe(recipes, 1)
view_recipes(recipes)   

# //////////////////////Save and load function

def save_recipes(recipes):
    # Make sure the data folder exists
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    
    # write recipes to the Json file
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(recipes, file, ensure_ascii=False, indent=4)
    print("Recipes saved successfully!")

save_recipes(recipes)

#//Load function
def load_recipes (): # Don't need to pass 'recipes' argument to the function, it will read from the file
    if not os.path.exists(FILE_PATH):
        return []  # If file doesn't exist, return empty list
    with open(FILE_PATH, "r", encoding="utf-8") as file:
     return json.load(file) # Read and return data from JSON file
print(load_recipes())

recipes = load_recipes()  # Read recipes from JSON file

