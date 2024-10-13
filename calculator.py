from unicodedata import numeric

art = '''
 _____________________
|  _________________  |                  
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''

print(art)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def calculator():
    should_accumulate = True
    num1 = float(input("Enter first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an Operation: ")
        num2 = float(input("Enter second number: "))
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue or type 'n' to start a new operation")

        if choice == "y":
           num1 = answer
        else:
            should_accumulate = False
            print("\n *20")
            calculator()

calculator()