# link : https://www.pythontutorial.net/python-basics/python-try-except-else/


"""
Learn how to use the try...except...else statement.

The try...except...else statement works as follows:

- If an exception occurs in the try clause,
  Python skips the rest of the statements in the try clause and the except statement execute.
- In case no exception occurs in the try clause, the else clause will execute.
- When you include the finally clause, the else clause executes after the try clause and before the finally clause.

"""

# Introduction to the try...except...else statement.

"""
The following example illustrates how to use 
the try...except...else clause develop a program that calculates the body mass index (BMI).
"""


# 1) Using try…except…else statement for control flow


def calculate_bmi(height, weight):
    return weight / height ** 2


def evaluate_bmi(bmi):
    if 18.5 <= bmi <= 24.9:
        return "healty"
    if bmi >= 25:
        return "overweight"

    return "underweight"


def main():
    try:
        height = float(input("Enter your height (meters) : "))
        weight = float(input("Enter your weight (kilograms) : "))

    except ValueError:
        print('Error! please enter a valid number.')

    else:
        bmi = round(calculate_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}.')
        print(f'This is considired {evaluation}.')


main()

# 2) Using Python try…except…else...finally example


fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
exit_state = False

while True:
    try:
        key = input("Enter a key lookup : ")
        fruit = fruits[key.lower()]
    except KeyboardInterrupt:
        break
    except KeyError:
        if key.lower() == 'exit':
            print(f'ini break {key.lower()}')
            break
        print(f'Error {key} does\'t exist.')
    else:
        print(fruit)
    finally:
        print('Press ctrl + c to exit.')
