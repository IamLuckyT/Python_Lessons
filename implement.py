#All the code for the lessons will be implemented here

grocery = ["2Kg Meat", "Pap", "Rice", "Spaghetti", "Mayo", "Tomato Sauce", "Wors", "Minced Meat", "Spices", "Soup", "Tin fish", "Baked Beans"]
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry"]
vegetables = ["Carrot", "Green Pepper", "Spinach", "Potato", "Cabbage", "Onion", "Garlic"]

userName = input("Enter your name: ")

print("Hey " + userName + ", from the grocery list, which items will you like to buy?")
print("You can choose from the following items:")
for fruit in fruits:
    print(fruit)

user_choice = input("Which fruit do you like? ")

if user_choice in fruits:
    print(f"You chose: {user_choice}")
else:
    print("Sorry, that fruit is not in the list.")


