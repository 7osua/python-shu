import random
# link : https://www.pythontutorial.net/python-basics/python-do-while/

"""
Python does not support the do:...while:... loop.
However, you can use the while loop and a break statement
to emulate the do:...while:... loop statement.

- Use a while: loop and the break statements 
  to emulate a do...while loop in Python
"""


# Introduction to the do:...while:... statement.


"""
- First, specify the condition as True in the while loop.
  This allows the code block to execute for the first time.
- Second, place a condition to break out of the while loop.
- The code block always executes at least one for the first time and 
  the condition is checked at the end of each iteration.
while True:
    
    if [condition]:
        break
"""

# Examples how to use the do:...while:... emulation.

"""
Develop a number guessing game:
1. Generate a random number within a range 1 to 10.
2. Then, repeatedly prompt users for entering a number.
   If the entered number is lower or higher than the random number,
   give a users a hint. If the entered number equals the random number,
   the while:... loops stops.
"""

MIN = 0
MAX = 10

secret_number = random.randint(MIN, MAX)

attempt = 0

# input_number = int(input(f'Enter a number between {MIN} and {MAX} : '))
# attempt += 1
#
#
# if input_number > secret_number:
#     print('It should be smaller.')
# elif input_number < secret_number:
#     print('It should be bigger.')
# else:
#     print(f'Bingo! {attempt} attempt\'s')


# while input_number != secret_number:
while True:
    attempt += 1
    input_number = int(input(f'Enter a number beetwen {MIN} and {MAX} : '))
    if input_number > secret_number:
        print('It should be smaller.')
    elif input_number < secret_number:
        print('It should be bigger.')
    else:
        print(f'Bingo! {attempt} attempt\'s')
        break
