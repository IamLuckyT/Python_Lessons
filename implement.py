#All the code for the lessons will be implemented here

grocery = ["2Kg Meat", "Pap", "Rice", "Spaghetti", "Mayo", "Tomato Sauce", "Wors", "Minced Meat", "Spices", "Soup", "Tin fish", "Baked Beans"]
fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Mango", "Pineapples", "Strawberry"]
vegetables = ["Carrots", "Green Peppers", "Spinach", "Potatoes", "Cabbages", "Onions", "Garlic"]

userName = input("Enter your name: ")

print("Hey " + userName + ", from the grocery list which items will you like to buy?")
print()

print("You can choose from the following grocery items:")
for item in grocery:
    print(item)

print()

print("NB : USE A COMMA TO SEPARATE YOUR CHOICES")

print()

user_choice = input("Select the item/items would you like to buy: ")

'''
if user_choice in fruits:
    print(f"You chose: {user_choice}")
else:
    print("Sorry, that fruit is not in the list.")
'''
# Split input by commas and strip whitespace

# Make comparison case-insensitive
grocery_lower = [item.lower() for item in grocery]
chosen_items = [item.strip() for item in user_choice.split(",")]
valid_choices = [grocery[grocery_lower.index(item.lower())] for item in chosen_items if item.lower() in grocery_lower]
invalid_choices = [item for item in chosen_items if item.lower() not in grocery_lower]

print(f"The items you want to buy are: {valid_choices}")

if invalid_choices:
    print(f"These items are not in the list and were ignored: {invalid_choices}")
    
print()

print("Here are fruits we have in stock:")

print()
for fruit in fruits:
    print(fruit)

print()

user_choice = input("Select fruits you would like to buy: ")

chosen_items = [item.strip() for item in user_choice.split(",")]


# Make comparison case-insensitive for fruits
fruits_lower = [fruit.lower() for fruit in fruits]
valid_choices = [fruits[fruits_lower.index(fruit.lower())] for fruit in chosen_items if fruit.lower() in fruits_lower]
invalid_choices = [fruit for fruit in chosen_items if fruit.lower() not in fruits_lower]

print(f"The fruits you want to buy are: {valid_choices}")

if invalid_choices:
    print(f"These fruits are not in the list and were ignored: {invalid_choices}")

Shops = []

print(userName + " please enter your davourite Shop(s)")

