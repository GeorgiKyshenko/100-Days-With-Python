alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# # inserting in list Tests
# text = alphabet.insert(2, ["a", "g", "d"])
# print(alphabet)
# print(alphabet[4])


def encrypt(input_text, input_shift):
    cipher_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + input_shift
            if new_position >= len(alphabet):
                new_letter = alphabet[((new_position - position) - ((len(alphabet) - 1) - position)) - 1]
            else:
                new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    print(f"The encrypted text is: {cipher_text}")


def decrypt(input_text, input_shift):
    decrypted_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - input_shift
            if new_position < 0:
                new_letter = alphabet[len(alphabet) - abs(new_position)]
            else:
                new_letter = alphabet[new_position]
            decrypted_text += new_letter
        else:
            decrypted_text += char
    print(f"The decrypted text is: {decrypted_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(
            input("Type the shift number:\n"))
        shift = shift % 26
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(
            input("Type the shift number:\n"))
        shift = shift % 26
        decrypt(text, shift)
    decision = input("If you want to continue press Y else, press N\n")
    if decision == "Y".casefold():
        continue
    elif decision == "N".casefold():
        break
