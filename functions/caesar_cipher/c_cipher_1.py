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


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("The shift number have to be less than 27. Anything above is considering too high for a cipher.\n"
                  "Type the shift number:\n"))

encrypt(text, shift)
