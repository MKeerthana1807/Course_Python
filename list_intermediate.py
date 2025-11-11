# ===== Task 1: Student Marks Analysis =====

# List of tuples: (Student Name, (Marks in 3 subjects))
students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]

# Step 1: Print each student's marks using nested loops
print("===== Student Marks Analysis =====")
for name, marks in students:
    print(f"{name}: ", end="")
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}", end=", " if i < len(marks) else "")
    print()

    # Step 2: Calculate average marks
    avg = sum(marks) / len(marks)
    print(f"Average Marks of {name}: {avg:.2f}")

    # Step 3: Find highest mark using tuple method
    highest = max(marks)
    print(f"Highest Mark of {name}: {highest}\n")

# Step 4: Add a new student and repeat steps
students.append(("David", (88, 76, 90)))

print("===== After Adding New Student =====")
for name, marks in students:
    print(f"{name}: ", end="")
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark}", end=", " if i < len(marks) else "")
    print()

    avg = sum(marks) / len(marks)
    print(f"Average Marks of {name}: {avg:.2f}")

    highest = max(marks)
    print(f"Highest Mark of {name}: {highest}\n")



# ===== Task 2: Grocery Store Inventory =====

# List of lists: [Category, [Items]]
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]

# Step 1: Print all categories and items using nested loops
print("===== Grocery Store Inventory =====")
for category, items in inventory:
    print(f"Category: {category}")
    for item in items:
        print(f" - {item}")
    print()

# Step 2: Add "Orange" to Fruits
for category, items in inventory:
    if category == "Fruits":
        items.append("Orange")

# Step 3: Remove "Spinach" from Vegetables
for category, items in inventory:
    if category == "Vegetables" and "Spinach" in items:
        items.remove("Spinach")

# Step 4: Count items in each category
print("===== Item Count in Each Category =====")
for category, items in inventory:
    print(f"{category}: {len(items)} items")

# Step 5: Print updated inventory
print("\n===== Updated Inventory =====")
for category, items in inventory:
    print(f"Category: {category}")
    for item in items:
        print(f" - {item}")
    print()
