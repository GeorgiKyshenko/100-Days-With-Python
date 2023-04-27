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
lives = 7

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        print(hangman_display.stages[lives - 1])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lost!\nThe word is: {concat_word(chosen_word)}")
    else:
        print(concat_word(display))
    if "_" not in display:
        end_of_game = True
        print("Congratulation! You guessed the word!")
