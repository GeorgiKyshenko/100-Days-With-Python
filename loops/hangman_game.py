import random

words = ["apple", "car", "dinosaur", "computer", "building", "chocolate", "beautiful"]
display = []
chosen_word = random.choice(words)

for _ in range(len(chosen_word)):
    display.append("_")

print(display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
print("You guessed the word!")

