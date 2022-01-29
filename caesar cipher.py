# The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.
# It’s simply a type of substitution cipher
# , i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.
# For example with a shift of 1, A would be replaced by B, B would become C, and so on.
# The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
# Thus, to cipher a given text we need an integer value, known as shift which indicates the number of position each
# letter of the text has been moved down.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)


def l2w(list2word):
    w = ""
    for char in list2word:
        w += char
    return w


def encrypt(user_input, shift_value):
    cipher_text = ""
    for letter in user_input:
        if letter == " ":
            new_letter = " "
            cipher_text += new_letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_value
            if new_position > 25:
                new_position = (new_position % 25) - 1
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    return cipher_text


def decrypt(user_input, shift_value):
    cipher_text = ""
    for letter in user_input:
        if letter == " ":
            new_letter = " "
            cipher_text += new_letter
        else:
            position = alphabet.index(letter)
            new_position = position - shift_value
            # print(new_position)
            if new_position < 0:
                new_position = (26 + new_position) % 26
                # print(new_position)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    return cipher_text


choice = input("Input E for encryption or D for decryption : ")
if choice in ["e", "E"]:
    message = input("Enter message to encrypt : ")
    shift = int(input("Input shift value : "))
    encrypted_text = encrypt(message, shift)
    print(f"After encryption : {encrypted_text}")
elif choice in ["d", "D"]:
    message = input("Enter message to decrypt : ")
    shift = int(input("Input shift value : "))
    decrypted_text = decrypt(message, shift)
    print(f"The decrypted text is {decrypted_text}")
else:
    print("Wrong input !!!")
