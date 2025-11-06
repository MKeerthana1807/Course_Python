
#Concatenate two strings
print("String Concatenation:")
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = str1 + str2
print("After concatenation:", result)


# Check if a string contains a specified sequence
print("\nSubstring Check:")
text = input("Enter main string: ")
sub = input("Enter substring to search: ")

if sub in text:
    print(f"'{sub}' is found in the given string.")
else:
    print(f"'{sub}' is not found in the given string.")


# Convert all characters to lowercase**
print("\nConvert to Lowercase:")
text = input("Enter a string: ")
print("Lowercase version:", text.lower())


# Trim leading and trailing spaces
print("\nTrim Leading and Trailing Spaces:")
text = input("Enter a string with spaces: ")
trimmed = text.strip()
print("Original:", repr(text))
print("Trimmed:", repr(trimmed))


# Reverse a string**
print("\nReverse a String:")
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


## Replace all spaces with underscores
print("\nReplace Spaces with Underscores:")
text = "Python is fun"
result = text.replace(" ", "_")
print(result)


#Create a string made of the middle three characters
print("\nMiddle Three Characters:")
s = "Python123"
mid = len(s) // 2
result = s[mid-1:mid+2]
print(result)


# Convert first and last letters to capital
print("\nCapitalize First and Last Letters:")
s = "python"
result = s[0].upper() + s[1:-1] + s[-1].upper()
print(result)


# Find the length of a given string
print("\nLength of a String:")
s = "Hello Python"
print("Length of string:", len(s))


# Count occurrences of a word
print("\nCount Occurrences of a Word:")
text = "I am New to this office but not New to Python"
count = text.count("New")
print("Number of 'New':", count)

#Remove digits from a string
print("\nRemove Digits from a String:")
s = "Python123"
result = "".join([ch for ch in s if not ch.isdigit()])
print(result)


#Count number of words in a string
print("\nCount Number of Words in a String:")
text = "Python is easy to learn"
words = text.split()
print("Word count:", len(words))

# Replace a specific character
print("\nReplace Specific Character:")
text = "The quick brown fox jumps over the lazy dog"
new_text = text.replace("dog", "fog")
print(new_text)

# Count vowels
print("\nCount Vowels in a String:")
s = "Python Programming"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

# Check if string has only whitespace
print("\nCheck if String has Only Whitespace:")
s = "   "
print(s.isspace())  # True if only spaces

# Remove all digits from a string
print("\nRemove All Digits from a String:")
s = "Hel123lo"
result = ''.join(ch for ch in s if not ch.isdigit())
print(result)


#### a) Length using `len()`
print("\nLength of the string:")
name = "Keerthana"
print(len(name))

#### b) Convert to uppercase
print("\nUppercase conversion:")
print(name.upper())

#### c) Convert to lowercase
print("\nLowercase conversion:")
print(name.lower())

#### d) Count occurrences of 'a'
print("\nCount occurrences of 'a':")
print(name.count('a'))

#### e) Check if starts with “Hello”
print("\nCheck if starts with 'Hello':")
print(name.startswith("Hello"))

#### f) Check if ends with “.com”
print("\nCheck if ends with '.com':")
print(name.endswith(".com"))

#### g) Find position of “Python”
print("\nFind position of 'Python':")
text = "I love Python programming"
print(text.find("Python"))

# g. Replace the word “Java” with “Python”
print("\nReplace 'Java' with 'Python':")
sentence = "I like Java programming."
print(sentence.replace("Java", "Python"))

# h. Remove extra spaces from both sides
print("\nRemove extra spaces from both sides:")
s = "   Hello World   "
print(s.strip())

# i. Capitalize first letter
print("\nCapitalize first letter:")
s = "hello world"
print(s.capitalize())

# j. Split sentence into words
print("\nSplit sentence into words:")
sentence = "Split this sentence"
print(sentence.split())

# k. Join list of words
print("\nJoin list of words:")
words = ["Python", "is", "fun"]
print(" ".join(words))

# l. Check if only alphabets
print("\nCheck if only alphabets:")
s = "HelloWorld"
print(s.isalpha())

# m. Check if only numbers
print("\nCheck if only numbers:")
s = "12345"
print(s.isdigit())

# n. Check if both letters and numbers
print("\nCheck if alphanumeric:")
s = "abc123"
print(s.isalnum())

# o. Check if all lowercase
print("\nCheck if all lowercase:")
s = "hello"
print(s.islower())

# p. Check if all uppercase
print("\nCheck if all uppercase:")
s = "HELLO"
print(s.isupper())

# q. Swapcase
print("\nSwapcase:")
s = "Hello World"
print(s.swapcase())

# r. Title case
print("\nTitle Case:")
s = "hello world"
print(s.title())

# s. Check if only spaces
print("\nCheck if only spaces:")
s = "   "
print(s.isspace())

# t. Count vowels in string
print("\nCount Vowels in String:")
s = "Hello World"
print(sum(1 for c in s.lower() if c in "aeiou"))

# u. Palindrome check
print("\nPalindrome Check:")
word = "madam"
print(word == word[::-1])

# v. Remove all digits
print("\nRemove All Digits:")
import re
s = "a1b2c3"
print(re.sub(r'\d', '', s))

# w. Replace spaces with underscores
print("\nReplace Spaces with Underscores:")
s = "replace spaces"
print(s.replace(" ", "_"))

# x. Extract only numbers
print("\nExtract Only Numbers:")
s = "abc123xyz"
print("".join([ch for ch in s if ch.isdigit()]))

# y. Print words starting with capital letter
print("\nWords Starting with Capital Letter:")
s = "Hello world Apple Banana cat"
print([w for w in s.split() if w[0].isupper()])

# z. Count freq of each letter
print("\nFrequency of Each Letter:")
from collections import Counter
s = "Hello World"
print(Counter(c.lower() for c in s if c.isalpha()))

# aa. Remove all punctuation
print("\nRemove All Punctuation:")
import string
s = "Hello, world!"
print("".join(c for c in s if c not in string.punctuation))

# bb. Email ends with gmail.com
print("\nCheck if Email Ends with '@gmail.com':")
email = "test@gmail.com"
print(email.endswith("@gmail.com"))

# cc. Reverse string without slicing
print("\nReverse String without Slicing:")
s = "Python"
reversed_s = ''.join(reversed(s))
print(reversed_s)
