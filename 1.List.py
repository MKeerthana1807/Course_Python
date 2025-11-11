# List
# 1. Create a list of 5 of your favorite fruits.
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

# 2. Add a new fruit to the list using a list method.
fruits.append("Pineapple")
print(fruits)

# 3. Remove one fruit from the list.
fruits.remove("Banana")
print(fruits)

# 4. Print the number of fruits in your list.
print("Number of fruits:", len(fruits))

# 5. Print all the fruits one by one using a for loop.
print("Fruits one by one:")
for fruit in fruits:
    print(fruit)

# 6. Reverse the list and print it.
fruits.reverse()
print("Reversed list:", fruits)

# 7. Sort the list alphabetically and print it.
fruits.sort()
print("Sorted list:", fruits)

# 8. Check if a particular fruit (like "Apple") is in the list.
if "Apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")

#Tuple

# 1. Create a tuple of 5 of your favorite colors.
colors = ("Red", "Blue", "Green", "Yellow", "Purple")
print(colors)

# 2. Print the first and last color from the tuple.
print("First color:", colors[0])
print("Last color:", colors[-1])

# 3. Find the length of the tuple.
print("Length of tuple:", len(colors))

# 4. Count how many times a particular color appears in the tuple.
print("Count of 'Blue':", colors.count("Blue"))

# 5. Print all colors one by one using a for loop.
print("Colors one by one:")
for color in colors:
    print(color)

# 6. Combine two tuples of colors and print the result.
more_colors = ("Black", "White")
combined = colors + more_colors
print("Combined tuple:", combined)

# 7. Find the maximum and minimum value from a tuple of numbers.
numbers = (10, 25, 5, 40, 15)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# 8. Try to change a value in the tuple and observe what happens.
colors = ("Red", "Blue", "Green", "Yellow", "Purple")
print("Original tuple:", colors)
# colors[0] = "Pink"
print("Tuples cannot be changed. If you try to modify them, Python will show an error.")
