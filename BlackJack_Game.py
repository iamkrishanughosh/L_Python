import random

initial_user_credits = 500
user_credits = initial_user_credits
user_wants_to_play = True


def bet_func():
    user_bet = int(input("Place your bet : "))
    return user_bet


def up(str_a):
    if str_a in ["Y", "y"]:
        b = True
    else:
        print(f"You cashed out {user_credits} coins.")
        b = False
    return b


# Function to deal a single card at a time.
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Function to calculate score for one instance.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Function to compare scores to declare the winner. Return string is used to notify the betting system about the
# results regarding win/loss/tie
def compare_scores(user, computer):
    if user > 21 and computer > 21:
        print("You went over. You lose 😤")
        return "L"

    if user == computer:
        print("Draw 🙃")
        return "T"
    elif computer == 0:
        print("Lose, opponent has Blackjack 😱")
        return "L"
    elif user == 0:
        print("You win with a Blackjack 😎")
        return "W"
    elif user > 21:
        print("You went over. You lose 😭")
        return "L"
    elif computer > 21:
        print("Opponent went over. You win 😁")
        return "W"
    elif user > computer:
        print("You win 😃")
        return "W"
    else:
        print("You lose 😤")
        return "L"


# Function to print final hands of both players. Don't mind me I'm laaaazy.
def show_final_scores(p1_cards, p1_score, p2_cards, p2_score):
    print("\n")
    print(f"Your final hand : {p1_cards} . Your Score {p1_score}")
    print(f"Computer's final hand : {p2_cards} . Computer Score {p2_score}")


# Function defines the game logic for a proper BlackJack game.
def game_logic():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards} . Your Score {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or user_score > 21:
            is_game_over = True
            show_final_scores(user_cards, user_score, computer_cards, computer_score)
            print(compare_scores(user_score, computer_score))
            break
        else:
            user_want_card = input("Do you want to draw another card ? (Y/N) : ")
            if user_want_card in ["Y", "y"]:
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 and computer_score < user_score:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards} . Your Score {user_score}")
        print(f"Computer's first card : {computer_cards} . Computer's score {computer_score}")

    show_final_scores(user_cards, user_score, computer_cards, computer_score)
    win_loss = compare_scores(user_score, computer_score)
    return win_loss


while user_credits > 0 and user_wants_to_play:
    print(f"You currently have {user_credits} coins.")
    bet = int(bet_func())
    while bet > user_credits:
        print(f"You cannot place bet of more than {user_credits} coins.")
        bet = int(bet_func())
    user_credits -= bet
    win_loss_4_bet = game_logic()
    if win_loss_4_bet in ["W", "w"]:
        user_credits = user_credits + (bet * 2)
        print(f"Yay !!! You now have {user_credits} coins.")
        user_play = input("Press Y to play again or Press N to cash-out : ")
        user_wants_to_play = up(user_play)
    elif win_loss_4_bet in ["T", "t"]:
        user_credits = user_credits + bet
        print(f"That's a draw. You still have {user_credits} coins.")
        user_play = input("Press Y to play again or Press N to cash-out : ")
        user_wants_to_play = up(user_play)
    else:
        user_credits = user_credits
        if user_credits > 0:
            print(f"Oh noooo !!! You now have {user_credits} coins left.")
            user_play = input("Press Y to play again or Press N to cash-out : ")
            user_wants_to_play = up(user_play)
        else:
            print(f"Oh Nooo !!! You ran out of coins.")
            user_wants_to_play = False
