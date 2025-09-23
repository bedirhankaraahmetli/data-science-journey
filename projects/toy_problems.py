# %%
# Number Guessing Game Toy Problem
"""
A simple number guessing game where the user has to guess a randomly generated number between 1 and 100.

Returns:
    _type_: _none
"""

import random


def number_guessing_game():
    number = random.randint(1, 100)
    attemps = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attemps += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(
                f"Congratulations! You've guessed the number {number} in {attemps} attempts."
            )
            break


number_guessing_game()

# %%
# Reverse String Toy Problem
"""
A simple function to reverse a given string.

Returns:
    _type_: _string
"""


def reverse_string(s):
    string = input("Enter a string to reverse: ")
    reversed = string[::-1]
    print(f"Reverse of the {string}: {reversed}")
    return reversed


reverse_string("Hello, World!")

# %%
# Basic Calculator Toy Problem
"""
A simple calculator that performs basic arithmetic operations like addition, subtraction, multiplication, and division.

Returns:
    _type_: _float
"""


def basic_calculator():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    try:
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            result = first_number / second_number
        else:
            print("Invalid operator!")
            return
        print(f"The result of {first_number} {operator} {second_number} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


basic_calculator()
# %%
# Fibonacci Sequence Toy Problem
"""
A function to generate the Fibonacci sequence up to n terms.

Returns:
    _type_: _list
"""
n = int(input("Enter the number of terms in the Fibonacci sequence: "))


def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    print(f"Fibonacci sequence with {n} terms: {fib_sequence[:n]}")
    return fib_sequence[:n]


fibonacci_sequence(n)


# %%
# Basic Grade Calculator Toy Problem
"""
A simple grade calculator that takes three grades as input and calculates the average. It then determines if the student has passed or failed based on the average.

Returns:
    _type_: _float
"""


def basic_grade_calculator():
    first_grade = float(input("Enter first grade: "))
    second_grade = float(input("Enter second grade: "))
    third_grade = float(input("Enter third grade: "))
    average = (first_grade + second_grade + third_grade) / 3
    if average >= 50:
        print(f"Congratulations! You passed!")
    else:
        print(f"Sorry! You failed!")
    print(f"Your average grade is: {average}")
    return average


basic_grade_calculator()
