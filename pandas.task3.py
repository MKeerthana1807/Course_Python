import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Age': [25, 30, 35, 40, 30, 25],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago'],
    'Salary': [50000, 60000, 70000, 80000, 60000, 50000]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# 1. Filter all employees with Salary > 60000
S = df[df['Salary'] > 60000]
print("\n1) Salary > 60000:\n", S)

# 2. Filter employees from Los Angeles and Age < 35
S2 = df[(df['City'] == 'Los Angeles') & (df['Age'] < 35)]
print("\n2) Los Angeles and Age < 35:\n", S2)

# 3. Group by City and find total Salary
S3 = df.groupby('City')['Salary'].sum()
print("\n3) Total Salary by City:\n", S3)

# 4. Group by Age and count employees for each age
S4 = df.groupby('Age')['Name'].count()
print("\n4) Employee Count by Age:\n", S4)

# 5. Group by City and find average Salary
S5 = df.groupby('City')['Salary'].mean()
print("\n5) Average Salary by City:\n", S5)

# 6. Plot a bar chart showing total Salary by City
S3.plot(kind='bar')
plt.title('Total Salary by City')
plt.xlabel('City')
plt.ylabel('Total Salary')
plt.show()

# 7. Plot a line chart for Salary values
df['Salary'].plot(kind='line', marker='o')
plt.title('Salary Line Plot')
plt.xlabel('Index')
plt.ylabel('Salary')
plt.show()

# 8. Plot a histogram for Age distribution
df['Age'].plot(kind='hist', bins=5)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.show()

# 9. Plot a pie chart showing percentage of employees by City
city_count = df['City'].value_counts()
city_count.plot(kind='pie', autopct='%1.1f%%')
plt.title('Employees by City (%)')
plt.ylabel('')  # removes extra y-label
plt.show()

# 10. Combine filtering and grouping:
# Find total Salary for employees with Age > 30 and plot a bar chart

filtered = df[df['Age'] > 30]
S10 = filtered.groupby('City')['Salary'].sum()
print("\n10) Total Salary by City (Age > 30):\n", S10)

S10.plot(kind='bar')
plt.title('Total Salary by City (Age > 30)')
plt.xlabel('City')
plt.ylabel('Total Salary')
plt.show()
