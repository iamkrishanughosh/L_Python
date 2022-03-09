import random


# 1=Rock 2=paper 3=scissor


def inputs_for_the_game():
    rock_image = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper_image = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors_image = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    computer = random.randint(1, 3)
    player = 0
    raw_input = input("Enter R for Rock, P for Paper and S for Scissors : ").lower()
    if raw_input in ['r', 'rock']:
        player = 1
        print("You chose Rock.")
        print(rock_image)
    elif raw_input in ['p', 'paper']:
        player = 2
        print("You chose Paper.")
        print(paper_image)
    elif raw_input in ['s', 'scissors']:
        player = 3
        print("You chose Scissors.")
        print(scissors_image)
    else:
        print("Wrong Input. Pls try again.")
        inputs_for_the_game()
    if computer == 1:
        print("Computer chooses Rock.")
        print(rock_image)
    elif computer == 2:
        print("Computer chooses Paper.")
        print(paper_image)
    else:
        print("Computer choose Scissors.")
        print(scissors_image)
    return [computer, player]


def rps_logic(ip):
    if ip == [1, 1] or ip == [2, 2] or ip == [3, 3]:
        print("Its a TIE.")
    elif ip == [1, 3] or ip == [2, 1] or ip == [3, 2]:
        print("Computer wins.")
    else:
        print("You win.")


the_inputs = inputs_for_the_game()
rps_logic(the_inputs)
