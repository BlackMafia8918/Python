height = float(input("Enter height in metres: "))
weight = int(input("Enter weight in kilograms: "))

BMI = round(weight/(height**2))

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal Weight")
elif BMI < 30:
    print("Overweight")
elif BMI < 35:
    print("Obese")
else:
    print("Clinically Obese")

print(BMI)