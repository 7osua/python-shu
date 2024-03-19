'''
link : https://www.pythontutorial.net/python-basics/
-----------------------------------------------------
learn about Python comparison operators and how to use them to compare two values.
'''

# Less than operator
x = 10
y = 20
print(f'x < y ? {x < y}')
print(f'y < x ? {y < x}')

print("'apple' < 'banana' = ", 'apple' < 'banana')
print("'banana' < 'apple' = ", 'banana' < 'apple')

# Less than or Equal To operator
print(f"20 <= 20 = {(20 <= 20)}")
print("10 <= 20 = ", (10 <= 20))
print("30 <= 30 = ", (30 <= 30))

x = 10
y = 20
print(f'x <= y = {x <= y}' )
print(f'y <= x = {y <= x}' )

# Greater than operator
print(f'20 > 10 = {20 > 10}')
print('20 > 20 = ', 20 > 20)
print('10 > 20 = ', 10 > 20)
print('orange > apple = ', ('orange' > 'apple'))
print('apple > orange = ', ('apple' > 'orange'))

# Greater than or equal to operator
print(f'20 >= 10 = {20 >= 10}')
print('20 >= 20 = ', 20 >= 20)
print('10 >= 20 = ', 10 >= 20)
print('apple >= apple = ', ('apple' >= 'apple'))
print('apple >= orange = ', ('apple' >= 'orange'))
print('orange >= apple = ', ('orange' >= 'apple'))


# Equal to operator
print(f'10 == 20  = {10 == 20}')
print(f'20 == 20  = {20 == 20}')
print('apple == apple = ', ('apple' == 'apple'))
print('apple == orange = ', ('apple' == 'orange'))

# Not Equal to operator
print('20 != 20', (20 != 20))
print('20 != 10', (20 != 10))
print('apple != apple = ', ('apple' != 'apple'))
print('apple != orange = ', ('apple' != 'orange'))
