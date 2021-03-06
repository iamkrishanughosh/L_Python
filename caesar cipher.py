# The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.
# It’s simply a type of substitution cipher
# , i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.
# For example with a shift of 1, A would be replaced by B, B would become C, and so on.
# The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
# Thus, to cipher a given text we need an integer value, known as shift which indicates the number of position each
# letter of the text has been moved down.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def l2w(list2word):
    w = ""
    for char in list2word:
        w += char
    return w


def encrypt(user_input, shift_value):
    cipher_text = ""
    for letter in user_input:
        if letter not in alphabet:
            new_letter = letter
            cipher_text += new_letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_value
            if new_position > 25:
                new_position = new_position % 25
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    return cipher_text


def decrypt(user_input, shift_value):
    cipher_text = ""
    for letter in user_input:
        if letter not in alphabet:
            new_letter = letter
            cipher_text += new_letter
        else:
            position = alphabet.index(letter)
            new_position = position - shift_value
            # print(new_position)
            if new_position < 0:
                # new_position = (26 + new_position) % 26
                new_position = new_position % 25
                # print(new_position)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    return cipher_text


def hack(user_input):
    for brute in range(1, 53):
        cipher_text = ""
        for letter in user_input:
            if letter not in alphabet:
                new_letter = letter
                cipher_text += new_letter
            else:
                position = alphabet.index(letter)
                new_position = position - brute
                if new_position < 0:
                    new_position = new_position % 25
                    # print(new_position)
                new_letter = alphabet[new_position]
                cipher_text += new_letter
        print(f"Encryption key {brute} : {cipher_text}")


choice = input("Input E for encryption or D for decryption or H for brute forcing any encryption: ")
while choice not in ["e", "E", "d", "D", "h", "H"]:
    print("Wrong Input. Try again.")
    choice = input("Input E for encryption or D for decryption or H for brute forcing any encryption: ")
if choice in ["e", "E"]:
    message = input("Enter message to encrypt : ")
    shift = input("Enter encryption key : ")
    while not shift.isnumeric():
        print("Encryption key should be a numeric input.")
        shift = input("Enter encryption key : ")
    shift = int(shift)
    encrypted_text = encrypt(message, shift)
    print(f"Encrypted message : {encrypted_text}\n")
elif choice in ["d", "D"]:
    message = input("Enter message to decrypt : ")
    shift = input("Enter encryption key : ")
    while not shift.isnumeric():
        print("Encryption key should be a numeric input.")
        shift = input("Enter encryption key : ")
    shift = int(shift)
    decrypted_text = decrypt(message, shift)
    print(f"The decrypted text : {decrypted_text}\n")
elif choice in ["H", "h"]:
    hack(input("Enter encrypted text : "))
else:
    print("Wrong input !!!")
