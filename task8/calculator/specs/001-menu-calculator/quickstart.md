# Quickstart Guide: Menu-Driven Basic Calculator

**Date**: 2025-12-02

## Overview

This guide provides instructions on how to quickly set up and run the Menu-Driven Basic Calculator CLI application.

## Prerequisites

*   **Python 3.x**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Running the Calculator

1.  **Navigate to the project root directory**:
    Open your terminal or command prompt and change your current directory to the root of this project.

    ```bash
    cd /path/to/your/calculator/project
    ```

2.  **Run the application**:
    Execute the Python application from your terminal:

    ```bash
    python src/calculator_cli.py
    ```

## Interacting with the Calculator

Once the application starts, you will see a welcome message and a menu of operations:

```
+-----------------------------------+
| Welcome to the Basic Calculator!  |
+-----------------------------------+
Please choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (x)
4. Division (/)
5. Exit
Enter your choice (1-5):
```

1.  **Choose an Operation**: Enter the number corresponding to your desired operation (1-5) and press Enter.
2.  **Enter Numbers**: Follow the prompts to enter the first and second numbers. The calculator will guide you through valid inputs.
3.  **View Result**: The calculation and its result will be displayed.
4.  **Continue or Exit**: You will be asked if you want to perform another calculation.
    *   Type `y` (or `Y`) and press Enter to return to the main menu.
    *   Type `n` (or `N`) and press Enter to exit the application.

## Example Session

```
+-----------------------------------+
| Welcome to the Basic Calculator!  |
+-----------------------------------+
Please choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (x)
4. Division (/)
5. Exit
Enter your choice (1-5): 1
Enter the first number: 10
Enter the second number: 5
10 + 5 = 15
Do you want to do another calculation? (y/n): y
Please choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (x)
4. Division (/)
5. Exit
Enter your choice (1-5): 4
Enter the first number: 20
Enter the second number: 0
You can't divide by zero! Please enter a different number.
Enter the second number: 4
20 / 4 = 5
Do you want to do another calculation? (y/n): n
Thank you for using the Basic Calculator! Goodbye!
```
