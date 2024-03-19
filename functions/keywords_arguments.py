'''
link: https://www.pythontutorial.net/python-basics/python-keyword-arguments/
-----------------------------------------------------------------------------
Learn about the Python keyword arguments, and how to use them to make function calls more obvious.
'''

def get_net_price(price, discount):
    return price * (1 - discount)

net_price = get_net_price(100, 0.1)
print(net_price)

"""
By using the keyword argument syntax, you don’t need to specify the arguments in the same order as defined in the function.
"""

net_price01 = get_net_price(discount = 0.2, price = 100)
print(net_price01)

net_price02 = get_net_price( price = 100, discount = 0.3)
print(net_price02)

net_price03 = get_net_price( 100, discount = 0.4)
print(net_price03)
