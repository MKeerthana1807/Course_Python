
# WHILE LOOP PROGRAMS

# Print numbers from 10 down to 1
print("=============numbers from 10 to 1================")
i = 10
while i >= 1:
    print(i)
    i -= 1

# Find the sum of even digits in a number
print("=============sum of even digits in a number================")
n = int(input("Enter a number: "))
sum_even = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_even += digit
    n //= 10
print("Sum of even digits:", sum_even)

#Count how many digits are in a number
print("=============count of digits in a number================")
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Total digits:", count)

#Check if a number is a palindrome
print("=============check if a number is palindrome================")
n = int(input("Enter a number: "))
temp = n
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n == rev:
    print("Palindrome")
else:
    print("Not palindrome")

#Find the reverse of a number
print("=============reverse of a number================")
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print("Reversed number:", rev)

#Print Fibonacci series up to 100
print("=============Fibonacci series up to 100================")
a, b = 0, 1
while a <= 100:
    print(a)
    a, b = b, a + b

#Compute power of a number (without ** or pow)
print("=============compute power of a number================")
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
i = 0
while i < exp:
    result *= base
    i += 1
print("Power:", result)

# Keep dividing by 2 until < 1 and count divisions
print("=============divide by 2 until less than 1================")
n = float(input("Enter a number: "))
count = 0
while n >= 1:
    n /= 2
    count += 1
print("Number of divisions:", count)

# Print digits of a number from last to first
print("=============digits of a number from last to first================")
n = int(input("Enter a number: "))
while n > 0:
    print(n % 10)
    n //= 10

#Compute the sum of squares of digits
print("=============sum of squares of digits================")
n = int(input("Enter a number: "))
sum_sq = 0
while n > 0:
    digit = n % 10
    sum_sq += digit ** 2
    n //= 10
print("Sum of squares of digits:", sum_sq)