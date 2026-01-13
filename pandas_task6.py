import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Temp": [30, 32, 31, 33, 34]
}
df = pd.DataFrame(data)

# Line chart
plt.plot(df["Day"], df["Temp"])
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Temperature Change Over Days")
plt.show()


#Bar Chart – Subjects & Marks
data = {
    "Subject": ["Math", "Science", "English"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)

plt.bar(df["Subject"], df["Marks"])
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Marks by Subject")
plt.show()

#Horizontal Bar Chart – Names & Salaries
data = {
    "Name": ["Ravi", "Anu", "Kiran"],
    "Salary": [30000, 28000, 35000]
}
df = pd.DataFrame(data)

plt.barh(df["Name"], df["Salary"])
plt.xlabel("Salary")
plt.ylabel("Name")
plt.title("Salary Distribution")
plt.show()


#Pie Chart – Product Sales Percentage
data = {
    "Product": ["A", "B", "C"],
    "Sales": [40, 35, 25]
}
df = pd.DataFrame(data)

plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()

#Line Chart with Markers – Monthly Profit
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Profit": [2000, 2500, 2200, 3000]
}
df = pd.DataFrame(data)

plt.plot(df["Month"], df["Profit"], marker="o")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit")
plt.show()

#Line Width Change
plt.plot(df["Month"], df["Profit"], linewidth=3)
plt.title("Line Width Example")
plt.show()


#Multiple Lines in One Graph
data = {
    "Student": ["A", "B", "C"],
    "Math": [80, 85, 78],
    "Science": [75, 88, 82]
}
df = pd.DataFrame(data)

plt.plot(df["Student"], df["Math"], label="Math")
plt.plot(df["Student"], df["Science"], label="Science")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Math vs Science Marks")
plt.legend()
plt.show()

#Same Data – Line & Bar Chart
data = {
    "Year": [2020, 2021, 2022],
    "Population": [50, 55, 60]
}
df = pd.DataFrame(data)

# Line chart
plt.plot(df["Year"], df["Population"])
plt.title("Population Growth - Line Chart")
plt.show()

# Bar chart
plt.bar(df["Year"], df["Population"])
plt.title("Population Growth - Bar Chart")
plt.show()

#GroupBy + Bar Chart
data = {
    "Student": ["A", "B", "C", "D"],
    "Department": ["IT", "IT", "HR", "HR"],
    "Marks": [80, 90, 70, 75]
}
df = pd.DataFrame(data)

# Group by department
avg_marks = df.groupby("Department")["Marks"].mean()

# Bar chart
avg_marks.plot(kind="bar")
plt.ylabel("Average Marks")
plt.title("Average Marks by Department")
plt.show()

import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [200, 250, 300, 280]
}

df = pd.DataFrame(data)

# Create CSV file
df.to_csv("sales.csv", index=False)

print("sales.csv file created")

df = pd.read_csv("sales.csv")
print(df)

df = pd.read_csv("sales.csv")

plt.plot(df["Month"], df["Sales"], marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
