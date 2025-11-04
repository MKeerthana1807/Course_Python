
# Print numbers between 1 and 100 that are divisible by 6 but not by 9
for i in range(1, 101):
    if i % 6 == 0 and i % 9 != 0:
        print(i)

#Find the sum of all odd numbers from 1 to 50
print("=============sum of odd numbers from 1 to 50================")
sum_odd = 0
for i in range(1,51,2):
    sum_odd +=i
    print(f"Sum of odd numbers up to {i} is {sum_odd}")
print(f"Total sum of odd numbers from 1 to 50 is {sum_odd}")

#Count how many numbers between 1 and 200 are divisible by both 4 and 6
print("=============count of numbers divisible by both 4 and 6================")
count=0
for i in range(1,201):
    if i%4==0 and i%6==0:
        count+=1
    print(f"{i} is {count}")
print(f"Total count {count}")

#Print multiplication table of a given number
print("=============multiplication table of a given number================")
num =int(input("Enter the number:"))  # You can change this number to generate table for a different number
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#Find factorial of a given number
print("=============factorial of a given number================")
factorial = 1
num = int(input("Enter a number to find its factorial: "))  # You can change this number
for i in range(1, num + 1):
    factorial *= i
    print(f"Factorial of {i} is {factorial}")
print(f"Total factorial of {num} is {factorial}")

#print all prime numbers between 1 and 50
print("=============prime numbers between 1 and 50================")
for num in range(2,51):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)


#Calculate sum of digits of a number
print("=============sum of digits of a number================")
number=int(input("Enter a number to calculate sum of its digits: "))  # You can change this number
sum_digits=0
for digit in str(number):
    sum_digits+=int(digit)
    print(f"Sum of digits up to {digit} is {sum_digits}")
print(f"Total sum of digits of {number} is {sum_digits}")

#Count how many numbers between 1 and 500 are perfect cubes
print("=============count of perfect cubes between 1 and 500================")
count_cubes=0
for i in range(1,501):
    cube=i**3
    if cube<=500:
        count_cubes+=1
        print(f"Perfect cube: {cube}, Count so far: {count_cubes}")
print(f"Total count of perfect cubes between 1 and 500 is {count_cubes}")

#Print reverse of a number
print("=============reverse of a number================")
n = int(input("Enter a number: "))
rev = 0
temp = n   # store original number for display

while n > 0:
    digit = n % 10         # get last digit
    rev = rev * 10 + digit # add digit to reversed number
    n //= 10               # remove last digit from n

print(f"Reverse of {temp} is {rev}")

#Print numbers 1–100 but skip numbers ending with 5
print("=============numbers from 1 to 100 skipping those ending with 5================")
for i in range(1,101):
    if i%10==5:
        continue
    print(i)

    