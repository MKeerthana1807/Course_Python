import pandas as pd
import numpy as np

#Create a DataFrame with missing values
data = {
    "Name": ["Alice", None, "Charlie", "David", None],
    "Age": [25, np.nan, 35, 30, np.nan],
    "City": ["Chennai", "Bangalore", None, "Hyderabad", "Chennai"],
    "Salary": [40000, 45000, 50000, 42000, 38000]
}

df = pd.DataFrame(data)
print(df)

#Check total missing values in each column
print(df.isnull().sum())

# Remove rows where City is missing
df = df.dropna(subset=["City"])
print(df)

# fill missing age values with the column average
df["Age"]= df["Age"].fillna(df["Age"].mean())
print(df)

#Replace missing name values with "unknown"
df["Name"] = df["Name"].fillna("unknown")
print(df)

# DataFrame Attributes
# print the shape of the dataframe
print("shape of dataframe:",df.shape)

# display all column names
print("column names:",df.columns)

# check the data types of each column
print("data types:\n", df.dtypes)

# set name as the index
df=df.set_index("Name")
print(df)

# reset the index back to default
df=df.reset_index()
print(df)

# sorting and updating data
# sort the dataframe by age is ascending order
df=df.sort_values(by="Age")
print(df)

# sort the dataframe by salary in descending order
df=df.sort_values(by="Salary",ascending=False)
print(df)

# increase salary by 5000 for employees whose age>30
df.loc[df["Age"]>30,"Salary"]=df["Salary"]+5000
print(df)

# replace "chennai" with "chennai city" in the city column
df["City"]=df["City"].replace("Chennai","Chennai City")
print(df)

# add a new row using .loc
df.loc[len(df)]=["Eve",28,"Mumbai",39000]
print(df)

# conditional selection and boolean logic
# display employees whose salary is greater than 40000
high_Salary=df[df["Salary"]>40000]
print(high_Salary)

# show only name and salary for employees in bangalore
bangalore_employees=df[df["City"]=="Bangalore"][["Name","Salary"]]
print(bangalore_employees)

# create a new colum status where salary>40000
df["Status"]=np.where(df["Salary"]>40000,"High","Low")
print(df)


# count how employees belong to each city
city_counts=df["City"].value_counts()
print(city_counts)

# select employees whose age is between 25 and 35
age_filtered=df[(df["Age"]>=25) & (df["Age"]<=35)]
print(age_filtered)

# import,export and viewing data 
# export the dataframe to a csv file
df.to_csv("employees_data.csv",index=False)

# import the csv file back into pandas
df_csv=pd.read_csv("employees_data.csv")
print(df_csv)

# display the first 5 rows using head
print(df.head())

# display the last 3 rows using tail
print(df.tail(3))

# check if the dataframe contains any missing values
print(df.isnull().any())

