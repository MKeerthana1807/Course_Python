
import pandas as pd

data = {
    "Name": ["Ravi", "Ravi", "Anu", "Anu", "Kiran", "Kiran"],
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
    "Salary": [30000, 32000, 28000, 29000, 35000, 36000]
}

df = pd.DataFrame(data)
print(df)

# Total and Maximum Salary for Each Employee
df.groupby("Name")["Salary"].agg(["sum", "max"])
print(df)

#Average Salary by Department (Descending Order)
df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(df)

# Department-wise Total Salary for **February**
df[df["Month"] == "Feb"].groupby("Department")["Salary"].sum()
print(df)

# Employees Whose Total Salary > 60,000
df.groupby("Name").filter(lambda x: x["Salary"].sum() > 60000)
print(df)

# Month-wise Total Salary for Each Department
df.groupby(["Department", "Month"])["Salary"].sum()
print(df)

#Department-wise Salary Count, Sum & Average
df.groupby("Department")["Salary"].agg(["count", "sum", "mean"])
print(df)

#Month with the Highest Total Salary
df.groupby("Month")["Salary"].sum().idxmax()
print(df)

# Add Department Average Salary Column (transform)
df["Dept_Avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")
df
print(df)

#Employees Paid Above Department Average
df[df["Salary"] > df.groupby("Department")["Salary"].transform("mean")]
print(df)

#Convert Department-wise Total Salary to Dictionary
df.groupby("Department")["Salary"].sum().to_dict()
print(df)