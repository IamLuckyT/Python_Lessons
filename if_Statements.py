userName = input("Hey, please enter your name: ")

print("Hello, " + userName) 

val = int(input("please add an number between 1 and 10: "))

if val > 10:
    print("You entered a number greater than 10")
elif val < 1:
    print("You entered a number less than 1")
else:
    print("Thanks, you entered the correct value")

val2 = int(input("Now enter a value between 10 and 20"))

if val2 > 20:
    print("You entered a number greater than 20")
else:
    print("Thanks, you entered the correct value")

print("Now we are going to compare the two values you entered")

if val > val2:
    print("The first value you entered is greater than the second value")
elif val < val2:
    print("The first value you entered is less than the second value")
else:
    print("The two values you entered are equal")

print("Now " + userName + " what else would you like to enter?")

