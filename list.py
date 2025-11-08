# 1. Reverse a given  list in python
print("============Reverse a given list in python============")
l=[100,200,300,400,500]
l.reverse()
print("Reversed List:",l)

# 2. concatenate two lists
print("============Concatenate two lists============")
list1=["Hello"," Madam"]
list2=["Dear"," Sir"]
list3=list1+list2
print("Concatenated List:",list3)

# 3. Remove empty strings from a list of strings
print("============Remove empty strings from a list of strings============")
list1=["pen","pencil","eraser","","scale"]
list2=[x for x in list1 if x!=""]
print("List after removing empty strings:",list2)

# 4. write a python program to convert a string to a list
print("============Convert a string to a list============")
string="Hello, welcome to the world of Python"
list1=string.split()
print("Converted List:",list1)

# 5. check if a list contains an element
print("============Check if a list contains an element============")
list=[1,2,3,'a', 'b', 'c']
element='a'
if element in list:
    print(f"The list contains the element: {element}")
else:
    print(f"The list does not contain the element: {element}")

# 6. remove all elements from a list
print("============Remove all elements from a list============")
list=[10,20,30,40,50]
list.clear()
print("List after removing all elements:",list)

# 7. count the occurrence of a specific object in a list
print("============Count the occurrence of a specific object in a list============")
pets=["dog","cat","fish","fish","cat"]
count_fish=pets.count("fish")
print("Number of times 'fish' occurs in the list:",count_fish)

# 8. return  the length of a list
print("============Return the length of a list============")
list=[1,2,3,4,5,6,7,8,9]
length=len(list)
print("Length of the list:",length)

# 9. insert a value at a specific index in an existing list
print("============Insert a value at a specific index in an existing list============")
list=[10,20,30,40,50]
list.insert(2,25)
print("List after inserting 25 at index 2:",list)

# 10. write a python program to clone or copy a list
print("============Clone or copy a list============")
original_list=[1,2,3,4,5]
cloned_list=original_list.copy()
print("Cloned List:",cloned_list)

# 11. write a python program to extend a list without append
print("============Extend a list without append============")
list1=[1,2,3]
list2=[4,5,6]
list1[len(list1):]=list2
print("Extended List:",list1)

# 12.remove duplicated from a list
print("============Remove duplicates from a list============")
numbers = [3, 2, 2, 1, 1, 1]
list_no_duplicates = []
for n in numbers:
    if n not in list_no_duplicates:
        list_no_duplicates.append(n)
print("List after removing duplicates:", list_no_duplicates)

# 13.find the index of the 1st matching element 
print("============Find the index of the 1st matching element============")
list=['a','b','c','d','e']
index_c=list.index('c')
print("Index of the first occurrence of 'c':",index_c)

# 14. check if an element is not in a list
print("============Check if an element is not in a list============")
list=[10,20,30,40,50]
element=25
if element not in list:
    print(f"The element {element} is not in the list.")
else:
    print(f"The element {element} is in the list.")

# 1.write a python program to create a list of 5 numbers and print it
print("============Create a list of 5 numbers and print it============")
numbers=[10,20,30,40,50]
print("List of 5 numbers:",numbers)

# 2. write a program to find the length of a list using len()
print("============Find the length of a list using len()============")
numbers=[10,20,30,40,50]
length=len(numbers)
print("Length of the list:",length)

# 3. write a program to access elements from a list using positive and negative index
print("============Access elements from a list using positive and negative index============")
numbers=[10,20,30,40,50]
first_element=numbers[0]
last_element=numbers[-1]
print("First element (positive index):",first_element)

# 4. write a program to update the 3rd element of a list
print("============Update the 3rd element of a list============")
numbers=[10,20,30,40,50]
numbers[2]=35
print("List after updating the 3rd element:",numbers)

# 5. write a program to delete an element from a list using del
print("============Delete an element from a list using del============")
numbers=[10,20,30,40,50]
del numbers[1]
print("List after deleting the 2nd element:",numbers)

# 6. write a program to append a new element to the list using append()
print("============Append a new element to the list using append()============")
numbers=[10,20,30,40,50]
numbers.append(60)
print("List after appending 60:",numbers)

# 7.write a program to insert an element at a specific position using insert()
print("============Insert an element at a specific position using insert()============")
numbers=[10,20,30,40,50]
numbers.insert(3,35)
print("List after inserting 35 at index 3:",numbers)

# 8. write a program to remove an element using remove()
print("============Remove an element using remove()============")
numbers=[10,20,30,40,50]
numbers.remove(30)
print("List after removing 30:",numbers)

# 9. write a program to remove the last element using pop()
print("============Remove the last element using pop()============")
numbers=[10,20,30,40,50]
last_element=numbers.pop()
print("Removed last element:",last_element)

# 10. write a program to clear all elements from a list using clear()
print("============Clear all elements from a list using clear()============")
numbers=[10,20,30,40,50]
numbers.clear()
print("List after clearing all elements:",numbers)

# 11. write a program to print all elements of a list using a for loop
print("============Print all elements of a list using a for loop============")
numbers=[10,20,30,40,50]
for num in numbers:
    print(num)

# 12. write a program to find the sum of all elements using sum()
print("============Find the sum of all elements using sum()============")
numbers=[10,20,30,40,50]
total=sum(numbers)
print("Sum of all elements in the list:",total)

# 13. write a program to find the maximum and minimum element in a list using max() and min()
print("============Find the maximum and minimum element in a list using max() and min()============")
numbers=[10,20,30,40,50]
maximum=max(numbers)
minimum=min(numbers)
print("Maximum element in the list:",maximum)
print("Minimum element in the list:",minimum)

#14. write a program to count how many times an element appears using count()
print("============Count how many times an element appears using count()============")
numbers=[10,20,30,20,40,20,50]
count_20=numbers.count(20)
print("Number of times 20 appears in the list:",count_20)

# 15. write a program to find the index of a specific element using index()
print("============Find the index of a specific element using index()============")
numbers=[10,20,30,40,50]
index_30=numbers.index(30)
print("Index of 30 in the list:",index_30)

# 16. write a program to reverse a list using reverse()
print("============Reverse a list using reverse()============")
numbers=[10,20,30,40,50]
numbers.reverse()
print("Reversed list:",numbers)

# 17. write a program to sort a list in ascending and descending order using sort()
print("============Sort a list in ascending and descending order using sort()============")
numbers=[50,20,40,10,30]
numbers.sort()
print("list sorted in ascending order:",numbers)
numbers.sort(reverse=True)
print("list sorted in descending order:",numbers)

# 18. write a program to copy one list to another using copy()
print("============Copy one list to another using copy()============")
numbers=[10,20,30,40,50]
copied_list=numbers.copy()
print("copied list:",copied_list)

# 19. write a program to print only even numbers from a list
print("============Print only even numbers from a list============")
numbers=[10,15,20,25,30,35,40,45,50]
even_numbers=[num for num in numbers if num%2==0]
print("Even numbers in the list:",even_numbers)

# 20. write a program to print only off numbers from a list
print("============Print only odd numbers from a list============")
numbers=[10,15,20,25,30,35,40,45,50]
odd_numbers=[num for num in numbers if num%2!=0]
print("Odd numbers in the list:",odd_numbers)

# 21. write a program to add two lists using + operators
print("============Add two lists using + operators============")
list1=[1,2,3]
list2=[4,5,6]
combined_list=list1+list2
print("Combined List:",combined_list)

# 22. write a program to repeat list elements using * operators
print("============Repeat list elements using * operators============")
list1=[1,2,3]
repeated_list=list1*3
print("Repeated List:",repeated_list)

# 23. write a program to check if an element exists in a list using in
print("============Check if an element exists in a list using in============")
list1=[10,20,30,40,50]
element=30
if element in list1:
    print(f"The element {element} exists in the list.")
else:
    print(f"The element {element} does not exist in the list.")

# 24. write a program to slice a list (print first 3 and last 3 elements)
print("============Slice a list (print first 3 and last 3 elements)============")
numbers=[10,20,30,40,50,60,70,80,90]
first_three=numbers[:3]
last_three=numbers[-3:]
print("First 3 elements:",first_three)
print("Last 3 elements:",last_three)

# 25. write a program to find the largest 2 numbers in a list
print("============Find the largest 2 numbers in a list============")
numbers=[10,20,50,40,30,60,80,70]
numbers.sort(reverse=True)
largest_two=numbers[:2]
print("Largest 2 numbers in the list:",largest_two)

# 26. write a program to find duplicate elements in a list
print("============Find duplicate elements in a list============")
del list 
numbers = [10, 20, 30, 20, 40, 30, 50, 10]
duplicates = set()
seen = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements in the list:", list(duplicates))

# 27. write a program to remove duplicate elements from a list
print("============Remove duplicate elements from a list============")
numbers=[10,20,30,20,40,30,50,10]
no_duplicates=list(set(numbers))
print("List after removing duplicates:",no_duplicates)

# 28. write a program to merge two sorted lsits in to one sorted list
print("============Merge two sorted lists into one sorted list============")
list1=[10,30,50,70]
list2=[20,40,60,80]
merged_list=sorted(list1+list2)
print("Merged sorted list:",merged_list)

# 29. write a program to create a list squares of numbers from 1 to 10 using loop
print("============Create a list of squares of numbers from 1 to 10 using loop============")
squares=[]
for i in range(1,11):
    squares.append(i**2)
print("List of squares from 1 to 10:",squares)

# 30. writea program to separate even and odd numbers into two list
print("============Separate even and odd numbers into two lists============")
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[]
odd_numbers=[]
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:",even_numbers)
print("Odd numbers:",odd_numbers)

# 31. write a program to create a nested list (list inside a list)
print("============Create a nested list (list inside a list)============")
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print("Nested List:",nested_list)

# 32. write a program to access elements from a nested list
print("============Access elements from a nested list============")
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
element=nested_list[1][2]
print("Accessed element (2nd list, 3rd element):",element)

# 33. write a program to flatten a nested list(converted to one single list)
print("============Flatten a nested list (converted to one single list)============")
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
flattened_list=[item for sublist in nested_list for item in sublist]
print("Flattened List:",flattened_list)

# 34. write a program to find common elements between two lists
print("============Find common elements between two lists============")
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_elements=[item for item in list1 if item in list2]
print("Common elements between the two lists:",common_elements)

# 35. write a program to find elements present in one list but not in another
print("============Find elements present in one list but not in another============")
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
unique_to_list1=[item for item in list1 if item not in list2]
print("Elements present in list1 but not in list2:",unique_to_list1)

# 36. write a program to remove all occurrences of a specific element from a list
print("============Remove all occurrences of a specific element from a list============")
numbers=[10,20,30,20,40,20,50]
element_to_remove=20
numbers=[num for num in numbers if num!=element_to_remove]
print("List after removing all occurrences of 20:",numbers)

# 37. write a program to convert a list into a tuple
print("============Convert a list into a tuple============")
numbers=[10,200,30,40,50]
numbers_tuple=tuple(numbers)
print("converted tuple:",numbers_tuple)

# 38. write a program to find the average of list elements.
print("============Find the average of list elements============")
numbers=[10,20,30,40,50]
average =sum(numbers)/len(numbers)
print("Average of list elements:",average)

# 39. write a program to count positive, negative, and zero element in a list
print("============Count positive, negative, and zero elements in a list============")
numbers=[10,-5,0,20,-15,0,30]
positive_count=len([num for num in numbers if num>0])
negative_count=len([num for num in numbers if num<0])
zero_count=len([num for num in numbers if num==0])
print("Positive elements count:",positive_count)
print("Negative elements count:",negative_count)
print("Zero elements count:",zero_count)

# 40. write a program to find product of all elements in a list(without using math.prod())
print("============Find product of all elements in a list (without using math.prod())============")
numbers=[1,2,3,4,5]
product=1
for num in numbers:
    product*=num
print("Product of all elements in the list:",product)

