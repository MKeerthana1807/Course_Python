

#1. Right Triangle
print("===== Right Triangle Pattern =====")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# 2. Left Triangle
print("===== Left Triangle Pattern =====")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

# 3. Square
print("===== Square Pattern =====")
rows = 5
for i in range(rows):
    print("*" * rows)

# 4. Print 8 (pattern of 8)
print("===== Pattern of 8 =====")
rows = 7
for i in range(rows):
    if i == 0 or i == rows // 2 or i == rows - 1:
        print("*****")
    else:
        print("*   *")

# 5. Hollow Square
print("===== Hollow Square Pattern =====")
rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 6. Hollow Right Triangle
print("===== Hollow Right Triangle Pattern =====")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 7. Inverse Left Triangle
print("===== Inverse Left Triangle Pattern =====")
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * i)

# 8. Inverse Right Triangle
print("===== Inverse Right Triangle Pattern =====")
rows = 5
for i in range(rows, 0, -1):
    print("*" * i)

# 9. Mixed Patterns (as in image)
# (a) Number Pattern 1
print("===== Mixed Patterns =====")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# (b) Number Pattern 2
print("\nNumber Pattern 2:")
for i in range(1, 6):
    for j in range(1, 6 - i + 1):
        print(j, end=" ")
    print()

# (c) Number Pattern 3
print("\nNumber Pattern 3:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# (d) Alphabet Pattern 1
print("\nAlphabet Pattern 1:")
for i in range(6):
    print(chr(65 + i) * (i + 1))

# (e) Alphabet Pattern 2
print("\nAlphabet Pattern 2:")
ch = 65
for i in range(1, 6):
    for j in range(i):
        print(chr(ch), end="")
        ch += 1
    print()

# (f) Alphabet Pattern 3
print("\nAlphabet Pattern 3:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()
