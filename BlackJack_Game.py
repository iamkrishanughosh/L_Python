import random

user_credits = 500


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user, computer):
    if user > 21 and computer > 21:
        return "You went over. You lose 😤"

    if user == computer:
        return "Draw 🙃"
    elif computer == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user == 0:
        return "You win with a Blackjack 😎"
    elif user > 21:
        return "You went over. You lose 😭"
    elif computer > 21:
        return "Opponent went over. You win 😁"
    elif user > computer:
        return "You win 😃"
    else:
        return "You lose 😤"


def show_final_scores(p1_cards, p1_score, p2_cards, p2_score):
    print("\n")
    print(f"Your final hand : {p1_cards} . Your Score {p1_score}")
    print(f"Computer's final hand : {p2_cards} . Computer Score {p2_score}")


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
            quit()
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
    print(compare_scores(user_score, computer_score))


game_logic()
