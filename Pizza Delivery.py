print("Welcome to Pizzeria Cafe")
size = int(input("Enter size(Small, Medium or Large): "))
add_pepperoni = input("Want to add some pepperoni? (Y or N): ")
extra_cheese = input("Want to some extra cheese? (Y or N): ")

Small = "$15"
Medium = "$20"
Large = "$25"

pepperoni_for_small_pizza = "$2" 
pepperoni_for_medium_or_large_pizza = "$3" 

extra_cheese_for_any_size = "$1"

total = size + extra_cheese_for_any_size + pepperoni_for_small_pizza | pepperoni_for_medium_or_large_pizza