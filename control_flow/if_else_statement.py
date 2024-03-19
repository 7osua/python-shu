'''
link : https://www.pythontutorial.net/python-basics/python-if/
-------------------------------------------------------------------------
Learn how to use the Python if statement to execute a block of code based on a condition.
You use the if statement to execute a block of code based on a specified condition.
'''

age = input('Enter your age : ')
# "if" statement
if int(age) >= 18:
    print(f'You\'re {age}, you\'re eligible to vote')
    print("let's go and vote !")
# "if...else" statement
else:
    print(f'You\'re {age}, not eligible to vote')

# "if...elif...else..." statement

your_age = input('Your age : ')

if int(your_age) < 5 :
    ticket_price = 5
elif int(your_age) < 16 :
    ticket_price = 10
else :
    your_age = 18
    ticket_price = 18

print(f'You\'re {your_age}, You\'ll pay ${ticket_price} for the tikets.')
