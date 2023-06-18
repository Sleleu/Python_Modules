from typing import List

class Recipe:
    def __init__(self,
                 name: str,
                 cooking_lvl : int,
                 cooking_time : int,
                 ingredients : List[str],
                 description: str,
                 recipe_type: str):

        if cooking_lvl not in range(1, 6):
            raise ValueError("Cooking level error")
        if cooking_time < 0:
            raise ValueError("Bad value for cooking time")
        if recipe_type not in ["starter","lunch","dessert"]:
            raise ValueError("Recipe type need to be starter, lunch or dessert")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        

    def __str__(self):
        str = f"Recipe {self.name}:\n\
    - cooking_lvl: {self.cooking_lvl}\n\
    - cooking time: {self.cooking_time} minutes\n\
    - ingredients: {self.ingredients}\n\
    - description: {self.description}\n\
    - recipe_type: {self.recipe_type}\n"
        return str

try:
    tourte = Recipe("tourte", 5, 10, ["tomatoes", "chips"], "description here", "lunch")
    print(tourte)
except ValueError as Error:
    print(Error)
