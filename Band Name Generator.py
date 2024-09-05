def BNG():
    print("Welcome to Band Name Generator")

    a = input("What is your name?\n")
    print(a)

    b = input("What is your pet name?\n")
    print(b)

    band_name = f"{a} {b}"
    print("Your band name could be:", band_name)

BNG()