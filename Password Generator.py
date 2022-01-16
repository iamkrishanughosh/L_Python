import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("Enter the number of letters you would like in your password ?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist


def easy_mode():
    passw = ""
    for char in range(1, nr_letters + 1):
        passw += random.choice(letters)

    for char in range(1, nr_symbols + 1):
        passw += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        passw += random.choice(numbers)
    print(passw)


def impossible():
    passw = []
    for char in range(1, nr_letters + 1):
        passw.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        passw.append(random.choice(symbols))

    for char in range(1, nr_numbers + 1):
        passw.append(random.choice(numbers))
    # print(passw)
    newpass = shuffle_list(passw)
    # print(newpass)
    newpassstr = ""
    for new in newpass:
        newpassstr += new
    print(newpassstr)


easy_mode()
impossible()
