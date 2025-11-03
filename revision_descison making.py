

#1. Variables of different data types
# Different data types
a = 10          # int
b = 12.5        # float
c = "Keerthana" # str
d = True        # bool
e = [1, 2, 3]   # list

# Display variable and its type
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))


## 2. Print sentence using variables
name = "Keerthana"
age = 21
print(f"My name is {name} and my age is {age}.")

#3. Arithmetic operations
x = 10
y = 5

print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)


#4. Combine string & integer (using f-string)
name = "Ravi"
age = 20
print(f"{name} is {age} years old.")



#6.Arithmetic operators
num1 = 4
num2 = 3
num3 = 5

square = num1 ** 2
cube = num2 ** 3
average = (num1 + num2 + num3) / 3

print("Square:", square)
print("Cube:", cube)
print("Average:", average)

#7. Relational operators
a = 10
b = 20

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#8. Logical operators
num = 8

print("Positive and even:", num > 0 and num % 2 == 0)
print("Negative or zero:", num < 0 or num == 0)


#9. Swap two variables (without third variable)
a = 5
b = 10

a, b = b, a
print("After swapping: a =", a, ", b =", b)

#10. Greater or Equal check
x = 15
y = 20

if x > y:
    print("x is greater")
elif x == y:
    print("Both are equal")
else:
    print("y is greater")


#11. Even or Odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#12. Positive, Negative, or Zero
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#13. Grade system
mark = 88

if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")

#14. Leap year check
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#15. Vote eligibility
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print(f"Not eligible. Wait {18 - age} more years.")


#16. Largest of three numbers
a = 12
b = 25
c = 9

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#17. Nested if – positive + even/odd
num = 4

if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative or Zero")

#18. Nested if – Age group
age = 45

if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

#19. Vowel or Consonant
ch = 'e'

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")


#20. Subject marks + nested if
m1 = 85
m2 = 92
m3 = 88

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")
    avg = (m1 + m2 + m3) / 3
    if avg >= 90:
        print("Outstanding")
else:
    print("Fail")
