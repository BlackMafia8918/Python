print("Welcome to Pizzeria Cafe")

prices = {
    "Small" or "S" or "s": 15,
    "Medium" or "M" or "m": 20,
    "Large" or "L" or "L": 25
}
pepperoni_prices = {
    "Small" or "S" or "s": 2,
    "Medium" or "M" or "m": 3,
    "Large" or "L" or "L": 3
}
extra_cheese_price = 1

size = input("Enter size(Small, Medium or Large): ")
add_pepperoni = input("Want to add some pepperoni? (Y or N): ").strip()
extra_cheese = input("Want to some extra cheese? (Y or N): ").strip()

total = prices.get(size, 0) 

if add_pepperoni == 'Yes' or 'yes' or 'y' or 'Y':
    total += pepperoni_prices.get(size, 0)
if extra_cheese == 'Yes' or 'yes' or 'y' or 'Y':
    total += extra_cheese_price

print(f"Total bill for your order is: ${total}")
print("Thank you for visiting")