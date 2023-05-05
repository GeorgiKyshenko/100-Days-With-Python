a = int(input())
b = int(input())
max_generated_passwords = int(input())

char_A = chr(34)
char_B = chr(63)
current_password_generated = 0
password = ""

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if ord(char_A) + 1 > 55:
            char_A = chr(35)
        else:
            char_A = chr(ord(char_A) + 1)
        if ord(char_B) + 1 > 96:
            char_B = chr(64)
        else:
            char_B = chr(ord(char_B) + 1)
        password = char_A + char_B + str(x) + str(y) + char_B + char_A
        current_password_generated += 1
        print(password, end="|")
        if current_password_generated == max_generated_passwords:
            break
    if current_password_generated == max_generated_passwords:
        break
