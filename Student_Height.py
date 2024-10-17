# Finding Average using for loop
 
height = input("Enter the list of students height: ").split()
sum = 0
i = 0 
for n in range(0, len(height)):
    n = int(height[n])
    print(n)
    sum += n
    i += 1
    avg_height = int(sum/i)
print("Total height is: ", sum)
print("Total number of students is: ", i)
print("Average height is: ", avg_height)