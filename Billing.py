print("Hello, Welcome to our Rollercoaster")
bill = 0
height = int(input("Enter height (in cm): "))

if height >= 120:
    print("You can ride the RollerCoaster")
    age = int(input("Enter your age: ")) 
    if age <= 12:
        print("Child tickets are $5 each.")
        bill = 5    
    elif (age <= 18):
        print("Youth tickets are $7 each.")
        bill = 7
    elif (age > 44 and age < 56):
        print("Midlife crisis people tickets are free.")
    else:
        print("Adult tickets are $12 each.")
        bill = 12

    wants_photo = input("Want a photo? Y or N: ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is: ${bill}")
else:
    print("Can't ride")