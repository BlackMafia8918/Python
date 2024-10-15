row1 = ["🔲", "🔲", "🔲"]
row2 = ["🔲", "🔲", "🔲"]
row3 = ["🔲", "🔲", "🔲"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
pos = input("Where do you want to put the treasure?")
hor = int(pos[0])
ver = int(pos[1])

map[ver-1][hor-1] = "X"
print(f"{row1}\n{row2}\n{row3}")