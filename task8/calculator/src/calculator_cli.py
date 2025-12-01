# Temporary change to force a new commit for synchronization
# This line will be removed later.

# src/calculator_cli.py

import sys

# --- Constants for Styling ---
COLOR_BLUE = "\033[94m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_PURPLE = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_END = "\033[0m"

EMOJI_SMILE = "😊"
EMOJI_WINK = "😉"
EMOJI_OOPS = "😵"
EMOJI_GOODBYE = "👋"
EMOJI_CALC = "🧮"
EMOJI_STAR = "✨"

# --- T007 & T025: Function to display welcome banner ---
def display_welcome_banner():
    """
    Displays a friendly and colorful welcome message for the calculator.
    Task T007 (foundational) and T025 (polish).
    """
    banner_line = COLOR_BLUE + "+" + "-" * 33 + "+" + COLOR_END
    welcome_text = COLOR_BLUE + f"| Welcome to the Basic Calculator! {EMOJI_CALC} |" + COLOR_END
    
    print(banner_line)
    print(welcome_text)
    print(banner_line)
    print(COLOR_PURPLE + f"  Let's have some fun with numbers! {EMOJI_STAR}" + COLOR_END)

# --- T006 & T026: Function to display the main menu ---
def display_main_menu():
    """
    Displays the main operation menu to the user with consistent formatting.
    Task T006 (foundational) and T026 (polish).
    """
    print(COLOR_GREEN + f"\n{EMOJI_STAR} Please choose an operation: {EMOJI_STAR}" + COLOR_END)
    print(f"  {COLOR_CYAN}1. Addition      (+){COLOR_END}")
    print(f"  {COLOR_CYAN}2. Subtraction   (-){COLOR_END}")
    print(f"  {COLOR_CYAN}3. Multiplication(x){COLOR_END}")
    print(f"  {COLOR_CYAN}4. Division      (/){COLOR_END}")
    print(f"  {COLOR_RED}5. Exit          {EMOJI_GOODBYE}{COLOR_END}")

# --- T003 & T020: Function to get and validate numeric input ---
def get_valid_number(prompt):
    """
    Prompts the user for a number and keeps asking until a valid number (float) is entered.
    Includes a friendly error message for invalid input.
    Task T003 (foundational) and T020 (US3 - refinement).
    
    Args:
        prompt (str): The message to display to the user.
    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            user_input = input(COLOR_YELLOW + prompt + COLOR_END)
            return float(user_input)
        except ValueError:
            print(COLOR_RED + f"Oops! That's not a valid number. Please try again {EMOJI_SMILE}" + COLOR_END)

# --- T004 & T021: Function to get and validate menu choice ---
def get_valid_choice(min_val, max_val):
    """
    Prompts the user for a menu choice and keeps asking until a valid integer
    within the specified range is entered. Includes a friendly error message.
    Task T004 (foundational) and T021 (US3 - refinement).

    Args:
        min_val (int): The minimum valid choice (inclusive).
        max_val (int): The maximum valid choice (inclusive).
    Returns:
        int: The valid integer choice entered by the user.
    """
    while True:
        try:
            choice_str = input(COLOR_YELLOW + f"Enter your choice ({min_val}-{max_val}): " + COLOR_END)
            choice = int(choice_str)
            if min_val <= choice <= max_val:
                return choice
            else:
                print(COLOR_RED + f"Please choose only {min_val}, {min_val+1}, {min_val+2}, {min_val+3} or {max_val}! {EMOJI_OOPS}" + COLOR_END)
        except ValueError:
            print(COLOR_RED + f"That's not a valid option. Please enter a number. {EMOJI_OOPS}" + COLOR_END)

# --- T005: Function to perform arithmetic calculation ---
def perform_calculation(op_choice, num1, num2):
    """
    Performs the selected arithmetic operation on two numbers.
    Task T005 (foundational). Division by zero is handled externally.

    Args:
        op_choice (int): The integer choice representing the operation (1-4).
        num1 (float): The first number.
        num2 (float): The second number.
    Returns:
        float: The result of the calculation.
        str: The symbol of the performed operation.
    """
    result = None
    op_symbol = ""
    if op_choice == 1: # Addition
        result = num1 + num2
        op_symbol = "+"
    elif op_choice == 2: # Subtraction
        result = num1 - num2
        op_symbol = "-"
    elif op_choice == 3: # Multiplication
        result = num1 * num2
        op_symbol = "x"
    elif op_choice == 4: # Division
        result = num1 / num2
        op_symbol = "/"
    return result, op_symbol

# --- T009 & T023: Function to get yes/no input ---
def get_yes_no_input(prompt):
    """
    Prompts the user for a 'y' or 'n' input and keeps asking until a valid choice is made.
    Includes a friendly error message for invalid input.
    Task T009 (foundational) and T023 (US3 - refinement).

    Args:
        prompt (str): The message to display to the user.
    Returns:
        str: 'y' or 'n' in lowercase.
    """
    while True:
        user_input = input(COLOR_YELLOW + prompt + " (y/n): " + COLOR_END).lower()
        if user_input in ['y', 'n']:
            return user_input
        else:
            print(COLOR_RED + f"Please enter 'y' for yes or 'n' for no, it's super important! {EMOJI_OOPS}" + COLOR_END)

# --- T008 & T025: Function to display goodbye message ---
def display_goodbye_message():
    """
    Displays a friendly goodbye message.
    Task T008 (foundational) and T025 (polish).
    """
    print(COLOR_GREEN + f"\n{EMOJI_STAR} Thank you for using the Basic Calculator! Goodbye! {EMOJI_GOODBYE} {EMOJI_STAR}" + COLOR_END)

# --- Main calculator logic wrapped in a function ---
def main():
    """
    Main function to run the calculator application.
    Integrates all functional components and handles the main program loop.
    """
    display_welcome_banner() # T010

    while True: # T017: Main program loop
        display_main_menu() # T011
        op_choice = get_valid_choice(1, 5) # T011
        
        if op_choice == 5: # T017: Exit condition
            display_goodbye_message()
            break # Exit the program loop

        num1 = get_valid_number("Enter the first number: ") # T012
        num2 = get_valid_number("Enter the second number: ") # T013

        # T022: Division by zero check with re-prompting
        if op_choice == 4: # If operation is division
            while num2 == 0:
                print(COLOR_RED + f"Hey! I can't divide by zero, let's pick another second number {EMOJI_WINK}" + COLOR_END)
                num2 = get_valid_number("Enter the second number: ") # Re-prompt for second number

        result, op_symbol = perform_calculation(op_choice, num1, num2) # T014
        
        # Display calculation result (T014 & T026)
        print(COLOR_GREEN + f"\n{num1} {op_symbol} {num2} = {result}" + COLOR_END)

        # T018: Ask to continue with validation
        continue_choice = get_yes_no_input("Do you want to do another calculation?")
        if continue_choice == 'n': # T018: Exit condition
            display_goodbye_message()
            break # Exit the loop and program


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C (T027: friendly message)
        print(COLOR_RED + f"\n\nCalculator interrupted. Exiting gracefully. {EMOJI_GOODBYE}" + COLOR_END)
        sys.exit(0)