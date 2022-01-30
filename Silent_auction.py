auction_members = {}


def add_auction_members():
    print('\n' * 8000)
    print(f"Member {len(auction_members)+1}")
    member = input("Enter your name : ")
    bid = int(input("Enter your bid : $"))
    auction_members[member] = bid
    flag = input("Any other members left to bid ? (Y/N) : ")
    if flag in ["y", "Y"]:
        print('\n' * 8000)
        add_auction_members()
    else:
        max_bid()


def max_bid():
    winner = ""
    current_max_bid = 0
    for member, bid in auction_members.items():
        if bid > current_max_bid:
            current_max_bid = bid
            winner = member
    print(f"Winner is {winner} with a bid of ${current_max_bid}")


add_auction_members()
