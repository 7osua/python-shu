'''
link : https://www.pythontutorial.net/python-basics/python-ternary-operator/
--------------------------------------------------------------------------------
Learn about the Python ternary operator and how to use it to make your code more concise.
'''

age = input('Enter your age : ')

# Use the ternary operator to make your code more concise.
ticket_price = 20 if(int(age) >= 18) else 5

print(f'The ticket price is ${ticket_price}.')
