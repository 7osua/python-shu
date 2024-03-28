'''
link : https://www.pythontutorial.net/python-basics/python-dictionary-comprehension/
-------------------------------------------------------------------------------------
Learn about Python dictionary comprehension to transform or filter items in a dictionary.

A dictionary comprehension iterates over items of a dictionary and allows you
to create a new dictionary by transforming or filtering each item.

'''

# Introductio to dictionary comprehension

'''
Increase the price of each stock by 2%
'''

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {}
new_stocks_comprehension = {}
new_stocks_comprehension_if_expression = {}

for sym, prc in stocks.items():
    new_stocks[sym] = prc + (prc * (2/100))

# Using comprehension dictionary to assign new value from another dictionary
new_stocks_comprehension = { sym: (val * 1.02) for (sym, val) in stocks.items() }


# Using dictionary comprehension to filter a dictionary

'''
select stocks whose prices are greater than 200, you may use the following for loop:
'''

for sym,prc in stocks.items():
    if prc > 200:
        new_stocks_comprehension_if_expression[sym] = prc

new_stocks_comprehension_if_expression = {sym:prc for (sym, prc) in stocks.items() if prc > 200}

print(stocks)
print(new_stocks)
print(new_stocks_comprehension)
print(new_stocks_comprehension_if_expression)
