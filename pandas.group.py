
import pandas as pd

data = {
    "Name": ["Ravi", "Ravi", "Anu", "Anu", "Kiran", "Kiran"],
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
    "Salary": [30000, 32000, 28000, 29000, 35000, 36000]
}

df = pd.DataFrame(data)
print(df)


## Task 1: Total Salary by Department
df.groupby("Department")["Salary"].sum()
print(df)

# Task 2: Average Salary by Department
df.groupby("Department")["Salary"].mean()
print(df)

# Task 3: Count of Employees by Department
df.groupby("Department")["Name"].count()
print(df)

#Task 4: Max Salary in Each Department
df.groupby("Department")["Salary"].max()
print(df)

#Task 5: Min Salary in Each Department
df.groupby("Department")["Salary"].min()
print(df)

# Task 6: Total Salary by Name
df.groupby("Name")["Salary"].sum()
print(df)

#Task 7: Average Salary by Department and Month
df.groupby(["Department", "Month"])["Salary"].mean()
print(df)


# Task 8: Multiple Aggregations
df.groupby("Department")["Salary"].agg(["sum", "mean", "max", "min"])
print(df)


# Task 9: Rename Aggregated Columns
df.groupby("Department")["Salary"].agg(
    Total_Salary="sum",
    Average_Salary="mean",
    Max_Salary="max",
    Min_Salary="min"
).reset_index()

print(df)


# Task 10: Reset Index After GroupBy
# a) Reset index after sum
dept_salary = df.groupby("Department")["Salary"].sum().reset_index()
print(dept_salary)

# b) Department with highest total salary
dept_salary.loc[dept_salary["Salary"].idxmax()]
print(dept_salary)