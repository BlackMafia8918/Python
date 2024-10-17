import random
print("Welcome to PyPassword Generator!")
letters = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
l = int(input("How many letters you want in the password?\n"))
s = int(input("How many symbols you want in the password?\n"))
n = int(input("How many numbers you want in the password?\n"))
# Easy Format
password = ""
for char in range(1, l+1):
    password += random.choice(letters)  
    password += random.choice(symbols)
    password += random.choice(numbers)  
print(f"Your password is: {password}")
# Hard Format
password_list = []
for char in range(1, l+1):
    password_list.append(random.choice(letters))  
    password_list += random.choice(symbols)
    password_list += random.choice(numbers)
print(password_list)

random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")