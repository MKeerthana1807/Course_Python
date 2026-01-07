import pandas as pd

data = {
    "Name": ["Ravi", "Kiran", "Meena"],
    "Age": [22, 25, 28],
    "City": ["Chennai", "Bangalore", "Hyderabad"]
}

df = pd.DataFrame(data)
print(df)


df.to_csv("students.csv", index=False)


df_csv = pd.read_csv("students.csv")
df_csv.to_csv("students_output.csv", index=False)

print(df_csv)

data = {
    "EmpName": ["Arun", "Divya", "Suresh"],
    "Salary": [30000, 40000, 50000],
    "Dept": ["HR", "IT", "Finance"]
}

df_emp = pd.DataFrame(data)
print(df_emp)

df_emp.to_excel("employees.xlsx", index=False)

df_excel = pd.read_excel("employees.xlsx")
df_excel.to_excel("employees_output.xlsx", index=False)
print(df_excel)


data = {
    "Name": ["Alice", "Bob"],
    "Age": [22, 25],
    "City": ["Chennai", "Bangalore"]
}

df_json = pd.DataFrame(data)
print(df_json)

df_json.to_json("students.json", orient="records", indent=4)
df_from_json = pd.read_json("students.json")
df_from_json.to_json("students_output.json", orient="records", indent=4)
print(df_from_json)


import pandas as pd

data = {
    "Product": ["Pen", "Book"],
    "Price": [10, 50]
}

df = pd.DataFrame(data)

# Default orientation = columns
df.to_json("products.json")

print(df)
df_from_json = pd.read_json("products.json")
print(df_from_json)

data = {
    "Name": ["John", "Sara", "Mike"],
    "Age": [25, None, 30],
    "City": ["NY", "LA", None]
}

df = pd.DataFrame(data)

df_clean = df.dropna()

print(df_clean)


data = {
    "A": [1, None],
    "B": [None, None],
    "C": [None, None]
}

df = pd.DataFrame(data)

df_clean = df.dropna(how="all")

print(df_clean)

data = {
    "Name": ["Ravi", "Kiran"],
    "Age": [22, None],
    "City": ["Chennai", "Bangalore"]
}

df = pd.DataFrame(data)

df_clean = df.dropna(axis=1)

print(df_clean)

data = {
    "Name": ["Anna", "Tom", "Sam"],
    "Age": [21, None, 23],
    "City": ["Paris", "Rome", "Berlin"]
}

df = pd.DataFrame(data)

df_clean = df.dropna(subset=["Age"])

print(df_clean)

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, None, 25]
}

df = pd.DataFrame(data)

df.dropna(inplace=True)

print(df)


data = {
    "Student": ["Raj", "Priya", "Kumar"],
    "Marks": [85, None, 90],
    "City": ["Chennai", "Madurai", None]
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("students_marks.csv", index=False)

# Read CSV
df_csv = pd.read_csv("students_marks.csv")

# Remove rows where Marks is missing
df_clean = df_csv.dropna(subset=["Marks"])

# Export to Excel
df_clean.to_excel("students_marks_clean.xlsx", index=False)

print(df_clean)


data = {
    "Item": ["Laptop", "Mouse", None],
    "Price": [50000, None, 800]
}

df = pd.DataFrame(data)

# Export JSON
df.to_json("items.json")

# Read JSON
df_json = pd.read_json("items.json")

# Remove missing rows
df_clean = df_json.dropna()

# Save CSV
df_clean.to_csv("items_clean.csv", index=False)

print(df_clean)


data = {
    "Name": ["Ramesh", None, "Sita"],
    "Age": [None, 24, 26],
    "City": ["Delhi", None, "Mumbai"]
}

df = pd.DataFrame(data)

df_clean = df.dropna()

print(df_clean)


data = {
    "Employee": ["E1", "E2", "E3"],
    "Salary": [30000, None, 45000],
    "Dept": ["HR", "IT", "Finance"]
}

df = pd.DataFrame(data)

df_clean = df.dropna(subset=["Salary"])

print(df_clean)


data = {
    "Name": ["Leo", "Mia", None],
    "Age": [21, 22, 23]
}

df = pd.DataFrame(data)

df_clean = df.dropna()

df_clean.to_json("clean_people.json", orient="records", indent=4)

print(df_clean)


data = {
    "Name": ["Arjun", "Kavya", None, "Rohit"],
    "Age": [24, None, 26, 28],
    "City": ["Chennai", "Delhi", "Mumbai", None]
}

df = pd.DataFrame(data)

# Remove rows where Age is missing
df_clean = df.dropna(subset=["Age"])

# Save CSV
df_clean.to_csv("final_clean.csv", index=False)

# Save JSON (records)
df_clean.to_json("final_clean.json", orient="records", indent=4)

print(df_clean)

