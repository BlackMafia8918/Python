print("Welcome to Pizzeria Cafe")
prices = {
    "Small": 15,
    "Medium": 20,
    "Large" : 25
}

pepperoni_prices = {
    "Small": 2,
    "Medium": 3,
    "Large" : 3
}

extra_cheese_price = 1

size = input("Enter size(Small, Medium or Large): ").capitalize()

add_pepperoni = input("Want to add some pepperoni? (Y or N): ").strip().upper()
extra_cheese = input("Want to some extra cheese? (Y or N): ").strip().upper()

total = prices.get(size, 0) 

if add_pepperoni == 'Yes' or 'yes' or 'y' or 'Y':
    total += pepperoni_prices.get(size, 0)

if extra_cheese == 'Yes' or 'yes' or 'y' or 'Y':
    total += extra_cheese_price

print(f"Total bill for your order is: ${total}")

print("Thank you for visiting")