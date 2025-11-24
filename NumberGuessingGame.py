# calculator.py
# Simple Calculator: Addition, Subtraction, Multiplication, Division

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_number(prompt):
    """Safely read a number from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_menu():
    print("\n====== Simple Calculator ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("================================")


def main():
    print("🎯 Welcome to the Python Calculator!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("👋 Exiting... Thank you for using the calculator.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select from 1 to 5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            op_symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op_symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op_symbol = "*"
        else:  # choice == "4"
            result = divide(num1, num2)
            op_symbol = "/"

        print(f"\nResult: {num1} {op_symbol} {num2} = {result}")


if __name__ == "__main__":
    main()
