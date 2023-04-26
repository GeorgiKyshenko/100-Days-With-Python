import sys

scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = scores[0]

for score in range(1, len(scores)):
    if highest_score < scores[score]:
        highest_score = scores[score]
print(f"Example 1: The highest score is: {highest_score}")

# or ->

highest_score2 = -sys.maxsize
for score in scores:
    if highest_score2 < score:
        highest_score2 = score
print(f"Example 2: The highest score is: {highest_score2}")

# or ->

print(f"Example 3: The highest score is: {max(scores)}")
print(f"Example 3.1: The lowest score is: {min(scores)}")



