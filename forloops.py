grocery = ["2Kg Meat", "Pap", "Rice", "Spaghetti", "Mayo", "Tomato Sauce", "Wors", "Minced Meat", "Spices", "Soup", "Tin fish", "Baked Beans"]

for item in grocery:
  print(item)

print()                     #Create a gap by printing an empty statement
for item in grocery:
  if item == "Rice":
    break                   #Closes loop if Rice is found
    print(item)

print()  

for item in grocery:
  if item == "Rice":
    continue                #Skips the Rice and moves to the next item which is Spaghetti
    print(item)

print()  

for item in grocery:
  if item == "Rice":
    pass                    #Doesnt do anything to Rice and prints items as is
    print(item)

