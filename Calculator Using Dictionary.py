operations = ["+", "-", "*", "/"]


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def user_input():
    n1 = int(input("Enter the first number : "))
    for symbol in operations: print(symbol)
    o_symbol = input("Pick an operator from the list above : ")
    n2 = int(input("Enter the second number : "))
    return [n1, o_symbol, n2]


inputs = user_input()
num1 = inputs[0]
num2 = inputs[2]
answer = 0
operator_symbol = inputs[1]
print(f"{num1} {num2} {answer} {operator_symbol}")
