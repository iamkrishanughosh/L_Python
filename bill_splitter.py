totalBill = int(input("Enter total bill amount : ₹ "))
people = int(input("Number of people to split the bill : "))
tipPercentage = int(input("Percentage of tip : "))/100


def splitwithtip(bill, person, percent):
    share = (bill + (bill * percent)) / person
    print(f"Each person should pay ₹ {share:1.2f}")


splitwithtip(totalBill, people, tipPercentage)
