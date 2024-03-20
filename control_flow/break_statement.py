'''
link : https://www.pythontutorial.net/python-basics/python-break/
-----------------------------------------------------------------
learn about the Python break statement and how to use it to exit a loop prematurely.
'''

# 'break' statement with for loop
for index in range(11):
    print(f"if index = 3 will stop loop, currently the value is {index}.")
    if index == 3:
        break


for x in range(5):
    for y in range(5):
        if y > 1:
            break

        print(f"x = {x},y = {y}")

# 'break' statement with while loop

print('--help : type \'quit\' to exit.--')
while True:
    color = input('Enter your favorite colour : ')
    if color.lower() == 'quit':
        break
