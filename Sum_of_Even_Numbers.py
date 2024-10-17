# Sum of evem numbers
# Method 1

sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)

# Method 2
total = 0
for i in range(0, 101):
    if i%2 == 0:
        total += i
print(total)