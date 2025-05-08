"""
Code to test the shopping API.
03.04.2025
"""

import requests as re
base_url  = "http://127.0.0.1:8000"
response = re.get(f"{base_url}/shopping")
shopping_list = response.json()
print(f"{shopping_list}")

while True:
    data = input("Please enter the item and the amount seperated by space you want to add to the shopping list"
                 " (or 'end' to quit and 'clear' to clear the list: ")
    if data == "end":
        break
    elif data == "clear":
        response = re.delete(f"{base_url}/shopping")
        if response.status_code == 200:
            print("Shopping list cleared")
        else:
            print(f"Error clearing shopping list {response.status_code}")
    else:
        if len(data.split()) == 2:
            data = data.split()
            item = data[0]
            amount = int(data[1])
            response = re.post(f"{base_url}/shopping?item={item}&amount={amount}")
        else:
            response = re.post(f"{base_url}/shopping?item={data}")
        if response.status_code == 200:
            print(f"Item '{data}' added to shopping list")
        else:
            print(f"Error adding item '{data}' to shopping list. ")

response = re.get(f"{base_url}/shopping")
shopping_list = response.json()
print(f"{shopping_list}")