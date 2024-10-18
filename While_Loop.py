# Reeborg's World Python Game Hurdle1 Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
# Method 1
for step in range(6):
    jump()
# Method 2
hurdles = 6
while hurdles > 0:
    jump()
    hurdles -= 1
    print(hurdles)