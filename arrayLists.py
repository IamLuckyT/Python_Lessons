grocery = ["2Kg Meat", "Pap", "Rice", "Spaghetti", "Mayo", "Tomato Sauce", "Wors", "Minced Meat", "Spices", "Soup", "Tin fish", "Baked Beans"]
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry"]
vegetables = ["Carrot", "Green Pepper", "Spinach", "Potato", "Cabbage", "Onion", "Garlic"]

fruits.append("Tomato")                     #Adds an item in the array
fruits.insert(1, "Watermelon")              #Adds watermelon on the 1st part of the items
fruits.remove("Tomato")                     #Removes tomato from the list
fruits.sort()                               #Sorts the items in alphabetical order
fruits.reverse()                            #Reverses the order of the items


userName = input("Enter your name: ")

print("Hey " + userName + ", from the grocery list, which items will you like to buy?")
print("You can choose from the following items:")

for item in grocery:
    print(item) # Accessing each item on the grocery list

for item in fruits:
    print(item) # Accessing each item on the fruits list

for item in vegetables:
    print(item) # Accessing each item on the vegetables list

