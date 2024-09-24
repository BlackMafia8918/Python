# Write a program that switches the value stored in the variable a and b without changing the input and output method

a = input("a: ")
b = input("b: ")

a,b = b,a

print("a:", a)
print("b:", b)