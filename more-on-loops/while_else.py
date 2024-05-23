# link : https://www.pythontutorial.net/python-basics/python-while-else/

"""
Learn about the while:...else:... statement and how to use it effectively.
-   The else clause in the while:...else:... statement will execute
    when the condition of the while loop is False and the loop runs normally
    without encountering the break or return statement.
"""


# Introduction to while:...else:... statement.

"""
1. Enter a fruit name, based on the input name.
2. Search a fruit name from the basket list.
3. Show its quantity if the fruit on the list.
4. In case the fruit name is not found, 
   we'll allow user to enter the quantity 
   for that fruit and add it to the list bucket.
"""
basket = [{'fruit': 'apple', 'quantity': 20},
          {'fruit': 'banana', 'quantity': 30},
          {'fruit': 'orange', 'quantity': 10}]


fruit = input('Enter a fruit : ')
quantity = 0;

index = 0
# found_it = False # if not found_it: # If not using while:...else:... statement


while index < len(basket):
    item = basket[index]

    if item['fruit'].lower() == fruit.lower():
        # found_it = True # If not using while:...else:... statement
        print(f"The basket has {item['quantity']} {item['fruit']}(s).")
        break
    index += 1
# if not found_it: # If not using while:...else:... statement
else:
    quantity = input(f'Enter the quantity of the {fruit} : ')
    basket.append({'fruit': fruit, 'quantity': float(quantity)})
    print(basket)
