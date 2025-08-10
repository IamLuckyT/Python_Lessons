#A tuple is a collection of objects that are ordered and immutable. 
#Tuples are similar to lists, but unlike lists, tuples cannot be changed after they are created. 
#Tuples can contain any type of object, including other tuples. 

my_tuples = (1, 2, 3, 4, 5)

for items in my_tuples:
    print(items)

print(my_tuples[0])  # Accessing the first element
print(my_tuples[-1])  # Accessing the last element
print(my_tuples[1:3])  # Slicing the tuple to get elements from index 1 to 2
print(len(my_tuples))  # Getting the length of the tuple
print(my_tuples.index(3))  # Finding the index of the element '3'
print(my_tuples.count(2))  # Counting occurrences of the element '2'

print()

# Tuples can also be nested
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Accessing the nested tuple (3, 4)
print(nested_tuple[2][0])  # Accessing the first element of the nested tuple
print(nested_tuple[2][1])  # Accessing the second element of the nested tuple
print(nested_tuple[2][0] + nested_tuple[2][1]) # Adding elements of the nested tuple

Print()

# Tuples can be concatenated and repeated
tuple1 = (1, 2, 3)
tuple1 += (4, 5)  # Concatenating another tuple
print(tuple1)  # Output: (1, 2, 3, 4, 5)
tuple2 = (6, 7)
tuple3 = tuple1 + tuple2  # Concatenating (Adding) two tuples
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6, 7)
tuple4 = tuple1 * 2  # Repeating the tuple
print(tuple4)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print()

# Tuples can be unpacked
a, b, c, d, e = my_tuples
print(a, b, c, d, e)  # Output: 1 2 3 4 5    
