"""
First FastAPI example creating a shopping list
03.04.2025
"""

from fastapi import FastAPI

app = FastAPI()

# the shopping list
shopping_list = {}


@app.get("/shopping")
async def get_shopping_list():
    for item, amount in shopping_list.items():
        print(f"{item}: {amount}")


@app.post("/shopping")
async def add_item(item: str, amount: int = 1):
    item = item.lower()
    shopping_list[item] = amount
    return {"OK"}


@app.delete("/shopping")
async def clear_list():
    shopping_list.clear()
    return {"OK"}
