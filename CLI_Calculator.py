# Simple Calculator Application

def calculator(num1, num2, operator):
    """
    Perform basic arithmetic operations based on the provided operator.
    :param num1: First operand (float)
    :param num2: Second operand (float)
    :param operator: Arithmetic operator (+, -, *, /)
    :return: Result of the operation or an error message
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        operator = input("Please choose from +, -, *, /: ").strip()
        return calculator(num1,num2,operator)

# Main loop to run the calculator continuously
print("Welcome to the CLI calculator")
while True:
    try:
        # Taking user input
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()

        # Performing the calculation
        result = calculator(first_number, second_number, operator)
        print(f"Result: {result}")

        # Prompt to continue or exit
        user_choice = input("Type 'Enter' to continue or 'Exit' to quit: ").lower().strip()
        if user_choice == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_choice != "enter":
            print("Invalid input. Continuing with calculator...")

    except ValueError:
        print("Input Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
