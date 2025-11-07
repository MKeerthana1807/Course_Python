# 1. Reverse a word
print("Reverse a Word:")
word = input("Enter a word: ")
reverse_word = word[::-1]
print("Reversed word:", reverse_word)

# 2. Count the number of letters in a string
print("Count Number of Letters in a String:")
string = input("Enter a string: ")
count = len(string)
print("Number of letters:", count)

# 3. Check whether an alphabet is a vowel or consonant
print("Check Vowel or Consonant:")
ch = input("Enter a single alphabet: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")

# 4. Find the median of three values
print("Find the Median of Three Values:")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

median = sorted([a, b, c])[1]
print("Median is:", median)


# 6. Check whether a number is an Armstrong number
print("Check Armstrong Number:")
num = int(input("Enter a number: "))
sum = 0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# 7. Find prime numbers up to a given limit
print("Find Prime Numbers up to a Given Limit:")
limit = int(input("Enter the limit: "))
print("Prime numbers up to", limit, "are:")

for num in range(2, limit + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

# 8. Check whether a number is a palindrome
print("Check Palindrome Number:")
num = input("Enter a number: ")

if num == num[::-1]:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
