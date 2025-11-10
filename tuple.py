

# 1. Create a tuple

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# 2. Find the size of a tuple
# Find size of a tuple
my_tuple = (10, 20, 30, 40)
print("Size of tuple:", len(my_tuple))


# 3. Sort tuples
# Sort a tuple
my_tuple = (5, 2, 8, 1, 9)
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple:", sorted_tuple)


# 4. Create a tuple with different data types
# Tuple with mixed data types
mixed_tuple = (10, "Hello", 3.5, True)
print("Tuple with different data types:", mixed_tuple)


# 5. Unpack a tuple into several variables
# Unpack tuple
student = ("Keerthana", 22, "Python")
name, age, course = student
print("Name:", name)
print("Age:", age)
print("Course:", course)

# 6. Convert a tuple to a string
# Convert tuple to string
tuple1 = ('P', 'y', 't', 'h', 'o', 'n')
string1 = ''.join(tuple1)
print("String:", string1)


# 7. Get 4th element and 4th from last element
# Access 4th and 4th from last element
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print("4th element:", my_tuple[3])
print("4th element from last:", my_tuple[-4])


# 8. Find repeated items in a tuple
# Find repeated items
my_tuple = (1, 2, 3, 2, 4, 3, 2)
repeated = [item for item in set(my_tuple) if my_tuple.count(item) > 1]
print("Repeated items:", repeated)

# 9. Check whether an element exists within a tuple
# Check element in tuple
my_tuple = (10, 20, 30, 40, 50)
print(30 in my_tuple)  # True

# 10. Convert a list to a tuple
# List to tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)

# 11. Remove an item from a tuple
# Remove an item from tuple (convert to list first)
my_tuple = (1, 2, 3, 4, 5)
temp_list = list(my_tuple)
temp_list.remove(3)
my_tuple = tuple(temp_list)
print("Tuple after removing 3:", my_tuple)

# 12. Slice a tuple
# Slice a tuple
my_tuple = (10, 20, 30, 40, 50, 60)
print("Sliced tuple:", my_tuple[2:5])

# 13. Find the index of an item in a tuple
# Index of an item
my_tuple = (10, 20, 30, 40, 30)
print("Index of 30:", my_tuple.index(30))

# 14. Find the length of a tuple
# Length of tuple
my_tuple = ('a', 'b', 'c', 'd')
print("Length:", len(my_tuple))

# 15. Reverse a tuple
# Reverse tuple
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print("Reversed tuple:", reversed_tuple)


#16. Convert a given string list to a tuple
# Convert string list to tuple
str_list = ['Python', 'is', 'fun']
result = tuple(str_list)
print("Tuple:", result)
