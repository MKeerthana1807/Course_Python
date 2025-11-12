#Prime numbers from 1 to 100
print("=== Prime numbers from 1 to 100 ===")

for n in range(2, 101):
    is_prime = True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")

print("\nPrime numbers printed successfully!\n")

#Number Pyramid Pattern
print("=== Number Pyramid Pattern ===")

rows = 5
for r in range(1, rows + 1):
    print("  " * (rows - r), end="")
    for inc in range(1, r + 1):
        print(inc, end=" ")
    for dec in range(r - 1, 0, -1):
        print(dec, end=" ")
    print()

# Electricity Bill Calculation
print("=== Electricity Bill Calculator ===")

units = float(input("Enter units consumed: "))
bill = 0.0
remaining = units

# 0–100 units
take = min(remaining, 100)
bill += take * 1.5
remaining -= take

# 101–200 units
if remaining > 0:
    take = min(remaining, 100)
    bill += take * 2.5
    remaining -= take

# 201–300 units
if remaining > 0:
    take = min(remaining, 100)
    bill += take * 4.0
    remaining -= take

# Above 300 units
if remaining > 0:
    bill += remaining * 5.0

# 10% surcharge if bill > ₹1000
if bill > 1000:
    bill *= 1.10

print(f"Total Bill = ₹{bill}")


# Diamond Star Pattern
print("=== Diamond Pattern ===")

n = 5
# Top half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Multiplication Table (1 to 10)
print("=== Multiplication Table 1 to 10 ===")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()

#Pascal’s Triangle
print("=== Pascal's Triangle ===")

n = 5
row = [1]
for i in range(n):
    print(" " * (n - i), end="")
    for val in row:
        print(val, end=" ")
    print()
    next_row = [1]
    for j in range(1, len(row)):
        next_row.append(row[j - 1] + row[j])
    next_row.append(1)
    row = next_row
