alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(input_text, input_shift):
    cipher_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position + input_shift
        if new_position >= len(alphabet):
            new_letter = alphabet[((new_position - position) - ((len(alphabet) - 1) - position)) - 1]
        else:
            new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encrypted text is: {cipher_text}")


def decrypt(input_text, input_shift):
    decrypted_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = position - input_shift
        if new_position < 0:
            new_letter = alphabet[len(alphabet) - abs(new_position)]
        else:
            new_letter = alphabet[new_position]
        decrypted_text += new_letter
    print(f"The decrypted text is: {decrypted_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(
            input("The shift number have to be less than 27. Anything above is considering too high for a cipher.\n"
                  "Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(
            input("Type the shift number:\n"))
        decrypt(text, shift)
    decision = input("If you want to continue press Y else, press N\n")
    if decision == "Y".casefold():
        continue
    elif decision == "N".casefold():
        break
