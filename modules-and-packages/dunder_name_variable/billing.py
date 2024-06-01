# link : https://www.pythontutorial.net/python-basics/python-__name__/

def calculate_tax(price, tax):
    return price * tax


def print_billing_docs():
    tax_rate = 0.1
    products = [{"name": "Book", "price": 30},
                {"name": "Pen", "price": 5}]
    # print billing header
    print('Name\tPrice\tTax')

    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f'{product["name"]}\t\t{product["price"]}\t\t{tax}')



if __name__ == '__main__':
    print(f'Running from : {__name__} => billing.py') # if the "billing" module run directly.
    print_billing_docs()
