# Dictionary to store recipes (key = recipe name in lowercase, value = recipe details)
recipes = {}

# Function 1: Greet and show commands


def greet():
    print("\nWelcome to the Digital Recipe Management App!")  # Welcome message
    print("Available commands:")  # Inform user about commands
    print(" > add recipe")        # Option to add recipe
    print(" > view recipes")      # Option to view all recipes
    print(" > search recipe")     # Option to search a specific recipe
    print(" > delete recipe")     # Option to delete a recipe
    print(" > exit")              # Option to exit program

# Function 2: Add a recipe


def add_recipe():
    name = input("Enter the recipe name: ").strip()  # Ask for recipe name
    # Ask for recipe type
    type_ = input("Enter the recipe type (e.g., Dessert, Main Dish): ").strip()

    # Ingredients section
    ingredients = []  # Create empty list for ingredients
    try:
        # Ask number of ingredients
        num_ingredients = int(input("How many ingredients? "))
    except ValueError:  # If user enters invalid input
        print("Invalid input! Please enter a number next time.")
        return  # Exit function if error
    for i in range(num_ingredients):  # Loop for each ingredient
        # Ask ingredient
        ingredient = input(f"Enter ingredient {i+1}: ").strip()
        ingredients.append(ingredient)  # Add ingredient to list

    # Steps section
    steps = []  # Create empty list for steps
    try:
        num_steps = int(input("How many steps? "))  # Ask number of steps
    except ValueError:  # If user enters invalid input
        print("Invalid input! Please enter a number next time.")
        return  # Exit function if error
    for i in range(num_steps):  # Loop for each step
        step = input(f"Enter step {i+1}: ").strip()  # Ask step
        steps.append(step)  # Add step to list

    # Store recipe details inside dictionary
    recipes[name.lower()] = {
        "name": name,            # Store original name
        "type": type_,           # Store recipe type
        "ingredients": ingredients,  # Store ingredients list
        "steps": steps               # Store steps list
    }

    print(f"Recipe '{name}' added!")  # Confirm recipe added


greet()
add_recipe()
