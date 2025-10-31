### 1️.Check whether a number is positive, negative, or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


### 2️. Check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")


### 3️. Check if a person is eligible to vote (age ≥ 18)
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


### 4️. Check if a student passed or failed based on marks
marks = float(input("Enter your marks: "))

if marks >= 40:
    print("Passed.")
else:
    print("Failed.")


### 5️. Find the largest of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(a, "is larger.")
else:
    print(b, "is larger.")

### 6️. Display grade (A, B, C, D, Fail) based on marks
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")


### 7️.Print the day name based on a number (1–7)
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid day number!")


### 8️. Check whether a character is an alphabet, digit, or special character
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

### 9️. Find the largest among three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the largest.")
elif b >= a and b >= c:
    print(b, "is the largest.")
else:
    print(c, "is the largest.")


### 10. Display message based on temperature
temp = float(input("Enter temperature in °C: "))

if temp > 35:
    print("It's Hot.")
elif temp > 25:
    print("It's Warm.")
elif temp > 15:
    print("It's Cool.")
else:
    print("It's Cold.")


### 11.Check whether a number is positive and even using nested if
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive and even.")
    else:
        print("Positive but odd.")
else:
    print("Not positive.")

### 12. Simulate a login system using nested if
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")

### 13️. Check if a person is eligible for a job
age = int(input("Enter age: "))
experience = input("Do you have experience? (yes/no): ").lower()

if age > 18:
    if experience == "yes":
        print("Eligible for the job.")
    else:
        print("Not eligible — no experience.")
else:
    print("Not eligible — age below 18.")


### 14 Check if a year is a leap year or not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")
else:
    print("Not a leap year.")

### 15️. Check whether a student qualifies for a scholarship
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

if marks >= 85 and attendance >= 90:
    print("Eligible for scholarship.")
else:
    print("Not eligible for scholarship.")
