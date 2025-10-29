a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

#1. Add Two Numbers
print("Addition:",a+b)

# 2. Subtract Two Numbers
print("Subtraction:",a-b)

#3. Multiply Two Numbers
print("Multiplication:",a*b)

#4. Divide Two Numbers
print("Division:",a/b)

# 5. Find Remainder
print("Modulus:",a%b)

# 6. Square of a Number
print("Square of first number:",a**2)

#7. Cube of a Number
print("cube of first number:",a**3)

#8. Average of Three Numbers
print("Average of three numbers:",a+(b+c)/3)

#9. Swap Two Variables
print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
print("\nAfter swapping:")
print("a =", b)
print("b =", c)
print("c =", a)

#10. Check Datatype
print("datatype of a:",type(a))


#11. Add Integer and Float
d=int(input("Enter integer value:"))
e=float(input("Enter float value:"))
print("Addition of integer and float:",d+e)
print("datatype after addition:",type(d+e))

# 12. Simple Comparison
print("Comparison Operators:")
print("a is greater than b:",a>b)

#13. Check Equal or Not
print("a is equal or not equal to b:",a!=b)

#14. Find Total and Average Marks
mark1= int(input("Enter first number:"))
mark2= int(input("Enter second number:"))
mark3= int(input("Enter third number:"))
mark4= int(input("Enter fourth number:"))
mark5= int(input("Enter fifth number:"))
average_marks= (mark1+mark2+mark3+mark4+mark5)/5
print("Average marks:",average_marks)

#15. Convert Hours to Minutes
hours=float(input("Enter hours worked:"))
minutes = hours * 60
print(f"{hours} hour(s) = {minutes} minute(s)")

#16. Calculate Simple Interest
principal = float(input("Enter Principal Amount (P): "))
rate = float(input("Enter Rate of Interest (R): "))
time = float(input("Enter Time in Years (T): "))
simple_interest = (principal * rate * time) / 100
print(f"\nSimple Interest = (P * R * T) / 100 = {simple_interest}")

#17. Find Area of a Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print(f"\nArea of Rectangle = {area}")

#18. Check Positive or Negative
num = float(input("Enter a number: "))
print("Is the number greater than 0?", num > 0)
print("Is the number less than 0?", num < 0)
print("Is the number equal to 0?", num == 0)

#19. Calculate Total Cost
cost = float(input("Enter cost of one item: "))
quantity = int(input("Enter number of items: "))
total = cost * quantity
print("Total Cost =", total)

#20. Small Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
