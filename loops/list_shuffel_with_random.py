import random
import string

chars = string.ascii_letters
symbols = string.punctuation
nums = string.digits

char_input = int(input("How many letter would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like?\n"))

password_list = []

# we can use append() or += it does the same !

for _ in range(char_input):
    password_list.append(random.choice(chars))

for _ in range(symbols_input):
    password_list += random.choice(symbols)

for _ in range(numbers_input):
    password_list += random.choice(nums)

# shuffle the password
random.shuffle(password_list)
password = ""

# concat the password_list elements into string password
for char in password_list:
    password += char
print(f"Your password is: {password}")
