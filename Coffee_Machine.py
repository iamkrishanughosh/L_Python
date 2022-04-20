on = True
resource_in_machine = {"Water": 500, "Milk": 400, "Coffee": 400, "Money": 0}
drink = {"espresso": {"Water": 75, "Milk": 10, "Coffee": 50, "Money": 30},
         "latte": {"Water": 150, "Milk": 75, "Coffee": 100, "Money": 70},
         "cappuccino": {"Water": 200, "Milk": 125, "Coffee": 125, "Money": 100}}

note_value = {"1": 1, "2": 2, "5": 5, "10": 10, "20": 20, "50": 50,
              "100": 100, "200": 200, "500": 500, "2000": 2000}


# print(drink['espresso']['Water'])
#
#
# def dic2list(dic):
#     list_val = list(dic.values())
#     return list_val
def add_resource():
    water = int(input("Add Water (ml) : "))
    milk = int(input("Add Milk (ml) : "))
    coffee = int(input("Add Coffee (gm) : "))
    print(f"Added {water} ml water, {milk} ml milk and {coffee} gm coffee in the machine.")
    return [water, milk, coffee]


while on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    while user_input not in ["espresso", "latte", "cappuccino", "off", "report", "add"]:
        print("Invalid Input")
        user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "off":
        print("Coffee Machine turned off.")
        on = False
    elif user_input == "report":
        print(f"\nResources in Machine : \nWater = {resource_in_machine['Water']} ml\n"
              f"Milk = {resource_in_machine['Milk']} ml\n"
              f"Coffee = {resource_in_machine['Coffee']} gm\n"
              f"Money = ₹ {resource_in_machine['Money']}\n")
    elif user_input == "add":
        resource_add_list = add_resource()
        resource_in_machine['Water'] = resource_in_machine['Water'] + resource_add_list[0]
        resource_in_machine['Milk'] = resource_in_machine['Milk'] + resource_add_list[1]
        resource_in_machine['Coffee'] = resource_in_machine['Coffee'] + resource_add_list[2]
    else:
        if resource_in_machine['Water'] < drink[user_input]['Water']:
            print("Sorry ! Not enough water.")
        elif resource_in_machine['Milk'] < drink[user_input]['Milk']:
            print("Sorry ! Not enough milk.")
        elif resource_in_machine['Coffee'] < drink[user_input]['Coffee']:
            print("Sorry ! Not enough Coffee.")
        else:
            print(f"Price of {user_input} is ₹{drink[user_input]['Money']}.")
            print("\nPay Here :")
            inr1 = int(input("Enter number of ₹ 1 notes/coins : "))
            inr2 = int(input("Enter number of ₹ 2 notes/coins : "))
            inr5 = int(input("Enter number of ₹ 5 notes/coins : "))
            inr10 = int(input("Enter number of ₹ 10 notes/coins : "))
            inr20 = int(input("Enter number of ₹ 20 notes : "))
            inr50 = int(input("Enter number of ₹ 50 notes : "))
            inr100 = int(input("Enter number of ₹ 100 notes : "))
            inr200 = int(input("Enter number of ₹ 200 notes : "))
            inr500 = int(input("Enter number of ₹ 500 notes : "))
            inr2000 = int(input("Enter number of ₹ 2000 notes : "))
            user_pay1 = (inr1 * note_value['1']) + (inr2 * note_value['2']) + (inr5 * note_value['5'])
            user_pay2 = (inr10 * note_value['10']) + (inr20 * note_value['20']) + (inr50 * note_value['50'])
            user_pay3 = (inr100 * note_value['100']) + (inr200 * note_value['200']) + (inr500 * note_value['500'])
            user_pay4 = (inr2000 * note_value['2000'])
            total_user_pay = user_pay1 + user_pay2 + user_pay3 + user_pay4
            if total_user_pay < drink[user_input]['Money']:
                print(f"Price of {user_input} is ₹{drink[user_input]['Money']}. Please enter appropriate amount.")
            else:
                return_user = total_user_pay - drink[user_input]['Money']
                money_in_machine = total_user_pay - return_user
                print(f"Change returned : ₹{return_user}")
                resource_in_machine['Water'] = resource_in_machine['Water'] - drink[user_input]['Water']
                resource_in_machine['Milk'] = resource_in_machine['Milk'] - drink[user_input]['Milk']
                resource_in_machine['Coffee'] = resource_in_machine['Coffee'] - drink[user_input]['Coffee']
                resource_in_machine['Money'] = resource_in_machine['Money'] + money_in_machine
                print(f"Enjoy your {user_input}. Thank You.")
