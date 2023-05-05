from art import logo
import sys


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 // n2


# we can pass functions names in a dictionary, and value of the key is the function with that name !
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}


# function = operations["*"]
# function(2, 3)
def calculation():
    num1 = float(input("Whats the first number?: "))
    for operator in operations:
        print(operator)

    is_calculation_finished = False
    while not is_calculation_finished:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("Whats the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        inpt = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, "
            f"or type 'exit' to terminate: ")
        if inpt == "y":
            num1 = answer
        elif inpt == "n":
            is_calculation_finished = True
            calculation()
        else:
            sys.exit()


print(logo)
calculation()
