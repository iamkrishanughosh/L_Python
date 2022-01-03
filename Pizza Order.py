print('''            88                                 
            ""                                                                                
8b,dPPYba,  88 888888888 888888888 ,adPPYYba,  
88P'    "8a 88      a8P"      a8P" ""     `Y8  
88       d8 88   ,d8P'     ,d8P'   ,adPPPPP88  
88b,   ,a8" 88 ,d8"      ,d8"      88,    ,88  
88`YbbdP"'  88 888888888 888888888 `"8bbdP"Y8  
88                                             
88''')

print("\n<<<<<<<<<<--Welcome to Hello World Pizza-->>>>>>>>>>\n")


# size = input("Size of Pizza (S, M, L) : ")
# pepperoni = input("Do you want pepperoni ? (Y or N) : ")
# cheese = input("Do you want extra cheese ? (Y or N) : ")

def pizza_order():
    price = 0
    size_tag = ""
    pepper_tag = ""
    cheese_tag = ""
    size = input("Size of Pizza (S - $15, M - $20, L - $25) : ")
    if size in ['S', 's', 'M', 'm', 'L', 'l']:
        if size in ['S', 's']:
            price += 15
            size_tag = "small"
        elif size in ['M', 'm']:
            price += 20
            size_tag = "medium"
        elif size in ['L', 'l']:
            price += 25
            size_tag = "large"
        pepperoni = input("Do you want to add pepperoni ? (Y or N) : ")
        if pepperoni in ['Y', 'y', 'N', 'n']:
            if pepperoni in ['Y', 'y']:
                pepper_tag = "with"
                if size in ['S', 's']:
                    price += 2
                elif size in ['M', 'm', 'L', 'l']:
                    price += 3
            else:
                pepper_tag = "with no"
            cheese = input("Do you want extra cheese for $1 ? (Y or N) : ")
            if cheese in ['Y', 'y', 'N', 'n']:
                if cheese in ['Y', 'y']:
                    price += 1
                    cheese_tag = "extra cheese"
                    print(f"\nYou ordered a {size_tag} {cheese_tag} pizza {pepper_tag} pepperoni.")
                    print(f"Please pay ${price}")
                else:
                    print(f"\nYou ordered a {size_tag} pizza {pepper_tag} pepperoni.")
                    print(f"Please pay ${price}")
            else:
                print("Invalid input. Please try again")
                pizza_order()
        else:
            print("Invalid input. Please try again")
            pizza_order()
    else:
        print("Invalid size input. Please try again")
        pizza_order()


pizza_order()
