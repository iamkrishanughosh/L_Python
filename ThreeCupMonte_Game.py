from random import shuffle

my_list = [' ', 'O', ' ']
print(f"Red ball is in middle cup now {my_list}")
print("About to shuffle")
guess = ''
while guess not in ['1', '2', '3']:
    guess = input("Pick a number 1,2,3 : ")


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess(p_guess):
    return int(p_guess) - 1


def never_win(mylist, p_guess):
    # Using this will never let the player win against computer
    if mylist[p_guess] == 'O':
        mylist[p_guess] = " "
        mylist[p_guess - 1] = "O"
    return mylist


def check_guess(mylist, i_guess):
    if mylist[i_guess] == 'O':
        print("Correct guess")
        print(mylist)
    else:
        print("Wrong guess")
        print(mylist)


mix_list = shuffle_list(my_list)
index_pick = player_guess(guess)
# never_win(mix_list,index_pick)
check_guess(mix_list, index_pick)
