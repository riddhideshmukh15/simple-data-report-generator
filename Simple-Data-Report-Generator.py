print("==== SIMPLE DATA REPORT GENERATOR ====")

data = []

n = int(input("How many values do you want to enter? "))

for i in range(n):
    value = float(input("Enter value: "))
    data.append(value)

total = sum(data)
average = total / len(data)
highest = max(data)
lowest = min(data)

print("\n=== DATA REPORT ===")

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Number of values:", len(data))