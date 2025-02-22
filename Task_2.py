# Calculator project
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}
# print(operations["*"](4,8))

def calculator():
    should_accumulate = True
    num1 = float(input("Enter the first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Choose a mathematical operation: ")
        num2 = float(input("Enter the second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation. ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20) # an illusion to clear the screen
            calculator() # recursion: calling function within the function itself
calculator()