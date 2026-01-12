import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [65, 78, 90, 55, 88],
    "Age": [20, 21, 22, 20, 23]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Find the average of the Marks column
average_marks = df["Marks"].mean()
print("Average Marks:", average_marks)


# Find the maximum marks scored
max_marks = df["Marks"].max()
print("Maximum Marks:", max_marks)

# Select students whose Marks are greater than 70
above_70 = df[df["Marks"] > 70]
print(above_70)

# Plot a bar chart for Name vs Marks
df.plot(x="Name", y="Marks", kind="bar")
plt.title("Marks of Students")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Add a new column Result (Pass / Fail)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(df)

# Count how many students passed and failed
result_count = df["Result"].value_counts()
print(result_count)

# Plot a pie chart for Pass vs Fail
result_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.ylabel("")  # hides extra label
plt.show()

# Plot a line chart for Age vs Marks
plt.plot(df["Age"], df["Marks"], marker="o")
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

# Create a horizontal bar chart for Name vs Marks
df.plot(x="Name", y="Marks", kind="barh")
plt.title("Marks of Students (Horizontal)")
plt.xlabel("Marks")
plt.ylabel("Name")
plt.show()
