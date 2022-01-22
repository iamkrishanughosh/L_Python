import random

word_list = ["elephant", "mouse", "turtle", "dog"]
word = random.choice(word_list).lower()


def create_blanks():
    blank = []
    for blnk in range(1, len(word) + 1):
        blank.append("_")
    return blank


blanks = create_blanks()
print(f"{blanks} Hint : Starts with the letter {word[0]}")

lives = len(word) - 1
life = 0
# print to test
print(lives)
# for life in range(0, lives):
while life < lives:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                blanks[position] = letter
                print(blanks)
    else:
        life += 1
        if life == lives:
            print("Wrong guess!!! \nGame Over !!! No lives left.")
        else:
            print(f"Wrong guess !!! {lives - life} lives left.")


