#Sets are used when you have a collection of unique elements

my_set = {1, 2, 3, 4, 5}
print(my_set}
      
print()
my_set.add(6)          #Adds 6 to the set
print(my_set)

print()
my_set.remove(3)
print(my_set)

print()
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}

#Union of sets
union_set = set1.union(set2)
print(union_set)
print()

#Intersection of sets
int_sets = set1.intersection(set2)
print(int_sets)
print()

#difference between sets
diff_sets = set1.difference(set2)
print(diff_sets)
print()
