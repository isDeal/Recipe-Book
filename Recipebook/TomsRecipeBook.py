#Tom's Recipe Book

#Imports

import time

import json

RECIPES_FILE = "recipes.json"

#Functions

def save_recipes():
    with open(RECIPES_FILE, 'w') as file:
        json.dump(recipes, file)

def load_recipes():
    try:
        with open(RECIPES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def view_recipe(name):
    if name in recipes:
        print("Recipe:", name)
        print("Ingredients:", ', '.join(recipes[name]['ingredients']))
        print("Instructions:", recipes[name]['instructions'])
    else:
        print("Recipe not found.")

def edit_recipe(name):
    if name in recipes:
        print("Editing", name)
        ingredients = input("Enter updated ingredients (comma-separated): ").split(',')
        instructions = input("Enter updated instructions: ")
        recipes[name] = {"ingredients": [ing.strip() for ing in ingredients], "instructions": instructions}
        print(f"{name} recipe updated successfully.")
        save_recipes()
    else:
        print("Recipe not found.")

def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    instructions = input("Enter instructions: ")
    
    recipes[name] = {"ingredients": [ing.strip() for ing in ingredients], "instructions": instructions}
    print(f"{name} recipe added successfully.")
    save_recipes()

# Load existing recipes when the application starts
recipes = load_recipes()

while True:
    print("\nRecipe Book Menu:")
    print("1. Search Recipes")
    print("2. Add Recipe")
    print("3. Edit Recipe")
    print("4. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        search_term = input("Enter the name of the recipe: ")
        matching_recipes = [name for name in recipes if search_term.lower() in name.lower()]
        if matching_recipes:
            print("Matching Recipes:")
            for idx, name in enumerate(matching_recipes, start=1):
                print(f"{idx}. {name}")
            recipe_choice = input("Enter the number of the recipe to view: ")
            if recipe_choice.isdigit() and 0 < int(recipe_choice) <= len(matching_recipes):
                chosen_recipe = matching_recipes[int(recipe_choice) - 1]
                view_recipe(chosen_recipe)
            else:
                print("Invalid choice.")
        else:
            print("No matching recipes found.")
    
    elif choice == '3':
        recipe_name = input("Enter the name of the recipe to edit: ")
        edit_recipe(recipe_name)
    
    elif choice == '2':
        add_recipe()
    
    elif choice == '4':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")
