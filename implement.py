#All the code for the lessons will be implemented here

grocery = ["2Kg Meat", "Pap", "Rice", "Spaghetti", "Mayo", "Tomato Sauce", "Wors", "Minced Meat", "Spices", "Soup", "Tin fish", "Baked Beans"]
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry"]
vegetables = ["Carrot", "Green Pepper", "Spinach", "Potato", "Cabbage", "Onion", "Garlic"]

userName = input("Enter your name: ")

print("Hey " + userName + ", from the grocery list which items will you like to buy?")
print("You can choose from the following grocery items:")
for item in grocery:
    print(item)

print()

print("NB : Use a comma to separate items")

user_choice = input("Select the item/items would you like to buy: ")

'''
if user_choice in fruits:
    print(f"You chose: {user_choice}")
else:
    print("Sorry, that fruit is not in the list.")
'''
# Split input by commas and strip whitespace
chosen_items = [item.strip() for item in user_choice.split(",")]

# Check which chosen fruits are valid
valid_choices = [item for item in chosen_items if item in grocery]
invalid_choices = [item for item in chosen_items if item not in grocery]

print(f"The items you want to buy are: {valid_choices}")

if invalid_choices:
    print(f"These items are not in the list and were ignored: {invalid_choices}")

print()
for fruit in fruits:
    print(fruit)

print()
