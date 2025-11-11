# Task 1: Student Marks Analysis
# List of tuples: (Student Name, (Marks in 3 subjects))
students = [
    ("Alice", (85, 90, 78)),
    ("Bob", (75, 80, 82)),
    ("Charlie", (95, 88, 92))
]

# Function to display marks, average, and highest mark
def display_student_details(students_list):
    for name, marks in students_list:
        print(f"{name}: ", end="")
        for i, mark in enumerate(marks, start=1):
            print(f"Subject {i}: {mark}", end=", " if i < len(marks) else "")
        print()


        avg = sum(marks) / len(marks)
        print(f"Average Marks of {name}: {avg:.2f}")

    
        highest = max(marks)
        print(f"Highest Mark of {name}: {highest}\n")

# Step 1–3: Display initial student data
print("===== Student Marks Analysis =====")
display_student_details(students)

# Step 4: Add new student
students.append(("David", (88, 76, 90)))

# Repeat steps 1–3 for updated list
print("===== After Adding New Student =====")
display_student_details(students)


# Task 2: Grocery Store Inventory
# List of lists: [Category, [Items]]
inventory = [
    ["Fruits", ["Apple", "Banana", "Mango"]],
    ["Vegetables", ["Carrot", "Tomato", "Spinach"]],
    ["Dairy", ["Milk", "Cheese", "Yogurt"]]
]

# Function to display inventory
def display_inventory(inv):
    for category, items in inv:
        print(f"Category: {category}")
        for item in items:
            print(f" - {item}")
        print()

# Step 1: Print all categories and items
print("===== Grocery Store Inventory =====")
display_inventory(inventory)

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
display_inventory(inventory)
