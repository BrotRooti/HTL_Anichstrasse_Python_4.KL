"""
First API Script, using Cocktail API
20.03.2025
"""

import requests as re

response = re.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=mojito")
print(response.json())

print("The required ingredients for a Mojito are:")

for i in range(1, 10):
    ingredient = response.json()["drinks"][0][f"strIngredient{i}"]
    if ingredient:
        print(ingredient)
    else:
        break
print("\n\n")
print("Instructions:")
print(response.json()["drinks"][0]["strInstructions"])