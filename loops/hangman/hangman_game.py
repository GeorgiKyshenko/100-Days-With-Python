import random
import hangman_display


def concat_word(word):
    output = ""
    for char in word:
        output += char
    return output


words = ["apple", "car", "dinosaur", "computer", "building", "chocolate", "beautiful"]
display = []
chosen_word = random.choice(words)

for _ in range(len(chosen_word)):
    display.append("_")

print(concat_word(display))
end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    print(concat_word(display))
    if guess not in chosen_word:
        print(hangman_display.stages[lives])
        lives -= 1
        if lives < 0:
            end_of_game = True
            print("You lost!")
        else:
            print(concat_word(display))
            continue
    if "_" not in display and lives > 0:
        end_of_game = True
        print("You guessed the word!")
