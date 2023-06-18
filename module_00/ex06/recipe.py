cookbook = {
    "sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10 
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    },
}

def print_recipes():
    print('List of recipes in the cookbook:')
    for recipe in cookbook:
        print(" ", recipe)

def print_details(recipe):
    if recipe in cookbook:
        print(f"Recipe for {recipe}:")
        print(f"    Ingredients list: {cookbook[recipe]['ingredients']}")
        print(f"    To be eaten for {cookbook[recipe]['meal']}.")
        print(f"    Takes {cookbook[recipe]['prep_time']} minutes of cooking.")
    else:
        print("Sorry, this recipe does not exist.")

def del_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
        print(f'recipe {recipe} successfully deleted !')
    else:
        print('Sorry, this recipe does not exist.')

def add_recipe():
    name = ''
    while name == '':
        name = input(">>> Enter a name: \n")
    ingredients = []
    print('>>> Enter an ingredient:')
    while True:
        ingredient = input()
        if ingredient == '':
            break
        ingredients.append(ingredient)
    meal_type = ''
    while meal_type == '':
        meal_type = input(">>> Enter a meal type: \n")
    prep_time = ''
    while prep_time == '':
        prep_time = input(">>> Enter a preparation time: \n")
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal_type,
        'prep_time': prep_time,        
    }

def display_options():
    print("List of available option:")
    print(" 1: Add a recipe")
    print(" 2: Delete a recipe")
    print(" 3: Print a recipe")
    print(" 4: Print the cookbook")
    print(" 5: Quit")

def main():
    print("Welcome to the Python Cookbook !")
    display_options()
    while True:
        option = input("\nPlease select an option:\n>> ")
        if option == '1':
            add_recipe()
        elif option == '2':
            recipe = input('Please enter a recipe name to delete:\n>> ')
            del_recipe(recipe)
        elif option == '3':
            recipe = input('\nPlease enter a recipe name to get its details:\n>> ')
            print_details(recipe)
        elif option == '4':
            print_recipes()
        elif option == '5':
            print("\nCookbook closed. Goodbye !")
            exit()
        else:
            print("Sorry, this option does not exist.")
            display_options()


if __name__ == "__main__":
    main()