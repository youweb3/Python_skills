#Recipe Manager

A simple Python command-line application to manage your recipes.
Save, view, search, edit, and delete recipes with data persistence using JSON.

#Features:

.Add new recipes with title, ingredients, and instructions
.View all recipes in a formatted list
.Search recipes by title keyword
.Edit recipe title, ingredients, or instructions
.Delete recipes with confirmation
.All changes are automatically saved to data/recipes.js

#Requirements:

.Python 3.x

#How to Run:

1.Clone the repository or download the files
2.Make sure you have Python 3 installed
3.Open a terminal and navigate to the project folder
4.Run the main script:
-> python recipe_manager.py

#Usage:

.Enter numbers 1-6 to choose actions from the menu
.Ingredients must be comma-separated
.Press Enter to skip editing a field (title, ingredients, or instructions)

#Data Persistence
.Recipes are saved in data/recipes.json
.Folder data/ is automatically created if it does not exist

#Notes
.Input validation prevents empty titles, ingredients, or instructions
.Invalid menu choices and non-numeric inputs are handled gracefully