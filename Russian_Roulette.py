import random
name = input("Enter the friends name: ")
names = name.split(", ")
print(names)

#Mehtod 1 without using choice() function
choice = random.randint(0, len(names)-1)
payee = names[choice]
print(f"{payee} will pay the bills today.")

#Mehtod 2 with using choice() function
payee = random.choice(names)
print(f"{payee} will pay the bills today.")