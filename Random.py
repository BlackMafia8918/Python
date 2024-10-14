import random

random_int = random.randint(0, 10)
print(random_int)

# Printing a random float by default b/w 0 and 1
random_float = random.random()
print(random_float)

# To print a random float b/w a given range greater than 1, multiply the random float value with any value b/w the given range 
print(random_float * random_int)

