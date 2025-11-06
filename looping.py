# Program to display the first 10 natural numbers
print("----- Looping Programs -----")
print("First 10 Natural Numbers:")
for i in range(1, 11):
    print(i)

# Program to sum the first 10 natural numbers
print("\nSum of First 10 Natural Numbers:")
sum_num = 0
for i in range(1, 11):
    sum_num += i
print("Sum of first 10 natural numbers is:", sum_num)

# Display n terms of natural numbers and their sum
print("\nDisplay n terms of natural numbers and their sum:")
n = int(input("Enter n: "))
sum_num = 0
for i in range(1, n + 1):
    print(i)
    sum_num += i
print("Sum =", sum_num)


# Display the first 10 natural numbers and find their sum and average
print("\nFirst 10 Natural Numbers with Sum and Average:")
sum_num = 0
for i in range(1, 11):
    sum_num += i
avg = sum_num / 10
print("Sum =", sum_num)
print("Average =", avg)


# Display the cube of the first 10 natural numbers
print("\nCube of the first 10 natural numbers:")
for i in range(1, 11):
    print(f"Number is {i} and cube of {i} is {i**3}")


#Display multiplication table of a given integer
print("\nMultiplication Table:")
n = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


# Calculate the factorial of a given number
print("\nFactorial Calculation:")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is {fact}")

#Display the n terms of harmonic series and their sum
print("\nHarmonic Series:")
n = int(input("Enter n: "))
sum_h = 0
for i in range(1, n + 1):
    print(f"1/{i}", end=" + ")
    sum_h += 1 / i
print("\nSum of harmonic series is:", round(sum_h, 2))

# Find numbers divisible by 7 and multiple of 5 between 1 and 100
print("\nDivisible by 7 and Multiple of 5:")
print("Numbers divisible by 7 and multiple of 5 (1–100):")
for i in range(1, 101):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Count number of even and odd numbers from a series
print("\nCount Even and Odd Numbers:")
n = int(input("Enter range limit: "))
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# Find numbers and sum of all integers between 100 and 200 divisible by 9
print("\nNumbers Divisible by 9 between 100 and 200:")
sum_div = 0
print("Numbers divisible by 9 between 100 and 200:")
for i in range(100, 201):
    if i % 9 == 0:
        print(i)
        sum_div += i
print("Sum of numbers divisible by 9 is:", sum_div)


#FizzBuzz (1 to 50)
print("\nFizzBuzz from 1 to 50:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=",")
    elif i % 3 == 0:
        print("Fizz", end=",")
    elif i % 5 == 0:
        print("Buzz", end=",")
    else:
        print(i, end=",")
