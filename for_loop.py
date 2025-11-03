# 1. print number from 1 to 20
for i in range(1,21):
    print(i)

# 2. print all even numbers from 2 to 50
print("=============even numbers================")
for i in range(2,51,2):
    print(i)

# 3. print all odd numbers from 1 to 50
print("=============odd numbers================")
for i in range(1,51,2):
    print(i)


# 4. print the square of number from 1 to 15
print("=============square of numbers================")
for i in range(1,16):
    print(f"square of {i} is {i**2}")


# 5. print the cube of numbers from 1 to 10
print("=============cube of numbers================")
for i in range(1,11):
    print(f"cube of {i} is {i**3}")


#6. print numbers from  10 down to 1 in reverse order
print("=============reverse order================")
for i in range(10,0,-1):
    print(i)


#7.print multiplication table of 5
print("=============multiplication table of 5================")
for i in range(1,11):
    print(f"5 x {i} = {5*i}")


# 8.print all characters of a string one by one
print("=============characters in a string================")
my_string = "Keerthana"
for char in my_string:
    print(char)

# 9. print number divisible by 3 between 1 and 30
print("=============numbers divisible by 3================")
for i in range(1,31):
    if i%3==0:
        print(i)