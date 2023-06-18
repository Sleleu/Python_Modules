from typing import List

class Recipe:
    def __init__(self,
                 name: str,
                 cooking_lvl : int,
                 cooking_time : int,
                 ingredients : List[str], # List is for python < 3.9
                 description: str,
                 recipe_type: str):
        print("yo")
    
    def __str__(self):
        str = "teeest"
        return str

tourte = Recipe("sd", 1, 10, ["tomatoes", "chips"], "description here", "lunch")
print(tourte)
