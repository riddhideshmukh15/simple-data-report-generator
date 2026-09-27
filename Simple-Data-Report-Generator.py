print("==== SIMPLE DATA REPORT GENERATOR ====")

data = []

n = int(input("How many values do you want to enter? "))

for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    data.append(value)

total = sum(data)
average = total / len(data)
highest = max(data)
lowest = min(data)
data_range = highest - lowest

positive = 0
negative = 0
even = 0
odd = 0

for value in data:
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1

    if value % 2 == 0:
        even += 1
    else:
        odd += 1

above_average = 0

for value in data:
    if value > average:
        above_average += 1

percentage_above_average = (above_average / len(data)) * 100


print("\n========== DATA REPORT ==========")

print("Values:", data)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)
print("Range:", range if False else data_range)

print("\n--- Additional Information ---")
print("Number of values:", len(data))
print("Positive values:", positive)
print("Negative values:", negative)
print("Even values:", even)
print("Odd values:", odd)

print(
    "Percentage above average:",
    round(percentage_above_average, 2),
    "%"
)

print("================================")
