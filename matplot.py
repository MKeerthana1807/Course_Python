import pandas as pd
import matplotlib.pyplot as plt
marks = [50, 60, 70, 80, 90]
exams = [1, 2, 3, 4, 5]


#Student Marks Line Chart
plt.plot(exams, marks)
plt.xlabel("Exam Number")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()


# Draw a line chart for daily temperatures
days =[28,30,32,31,29]
plt .plot(days, color = 'red')
plt.title("Daily Temperatures")
plt.ylabel("Temperature")
plt.show()


# plot a line chart of runs scored
sales = [10, 20, 15, 25, 30]
plt.plot(sales, linewidth=4)
plt.title("Monthly Sales")
plt.show()

# create a line chart for runs scored
scores=[45,60,75,90]
plt.plot(scores,marker='o',markersize =10)
plt.title("Runs scored")
plt.show()

# plot a line chart for profit values use color green marker as square line width 3
profit = [5,15,10,20,25]
plt.plot(profit, color='green',marker='s',linewidth =3)
plt.title("profit values")
plt.show()

# create a  bar chart for subjects and marks: subjects- [maths, science, english] marks-[85,90,78]
subjects =["Maths","Science","English"]
marks = [85,90,78]
plt.bar(subjects,marks)
plt.title("subject marks")
plt.show()


# create a bar chart for product sales use blue color for bars
products=['A','B','C']
sales=[40,60,50]
plt.bar(products,sales,color='blue')
plt.title("product sales")
plt.show()

# horizontal bar chart
city=cities = ['Chennai', 'Madurai', 'Coimbatore']
population = [10, 5, 7]

plt.barh(city,population,color='orange')
plt.title('city population')
plt.show()

# create a pie chart for market share use different colors for each slice
values=[40,30,20,10]
companies=['A','B','C','D']
plt.pie(values,labels=companies,colors=["red","blue","green","yellow"],autopct='%1.1f%%')
plt.title("Market Share")
plt.show()

# create a pie chart showing time spend in a day
time = [8, 6, 4, 6]
labels = ['Sleep', 'Work', 'Study', 'Others']

plt.pie(time, labels=labels, autopct='%1.1f%%')
plt.title("Daily Time Spent")
plt.show()