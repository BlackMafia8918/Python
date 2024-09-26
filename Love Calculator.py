print("Welcome to Love Calculator")
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")
name = name1 + name2
lower_name = name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
print(love_score)
if (love_score <= 10) or (love_score >= 80):
    print(f"Your love score is {love_score}, you go together like coke and mentos.") 
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you both are alright together.") 
else:
    print(f"Your love score is {love_score}")