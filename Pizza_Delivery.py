print("Welcome to Pizzeria Cafe")
size = input("What size of Pizza do you want? (S, M or L): ")
add_pepperoni = input("Want to add some pepperoni? (Y or N): ").strip().upper()
extra_cheese = input("Want to some extra cheese? (Y or N): ").strip().upper()
bill = 0
if size == 'S' or 's':
    bill += 15
elif size ==  'M' or 'm':
    bill += 20
else:
    bill += 25
if add_pepperoni == 'Y' or 'y':
    if size == 'Y' or 'y':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y' or 'y':
    bill += 1
print(f"Total bill for your order is: ${bill}")
print("Thank you for visiting")