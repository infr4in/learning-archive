from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    exit = False
    while not exit:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calc == "n":
            exit = True
            calculator()
        else:
            num1 = answer


calculator()
