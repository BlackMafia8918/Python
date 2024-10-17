# Finding the maximum and minimum score using for loop

scores = input('Enter the list of scores: ').split()
for s in range(0, len(scores)):
    s = int(scores[s])
    print(s)

max_score = scores[0]
min_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score

print("Max Score: ", max_score)
print("Min Score: ", min_score)