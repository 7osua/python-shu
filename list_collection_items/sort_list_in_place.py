'''
link : https://www.pythontutorial.net/python-basics/python-sort-list/
----------------------------------------------------------------------
Learn how to use the List sort() method to sort a list.
- Use the List sort() method to sort a list in place.
- The sort() method sorts the string elements in alphabetical order and sorts the numeric elements from smallest to largest.
- Use the sort(reverse=True) to reverse the default sort order.
'''

# Examples List sort()
guest = ["James", "Marry", "John", "Patricia", "Robert", "Jennifer"]
print(guest)

guest.sort()
print(guest)

guest.sort(reverse=True)
print(guest)

# List sort() method to sort a list of numbers.
scores = [5, 7, 4, 6, 9, 8]
print(scores)

scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)

# Using the Python List sort() method to sort a list of tuples
companies = [('Google', 2019, 134.81), ('Apple', 2019, 260.2), ('Facebook', 2019, 70.7)]
print(companies)

def sort_key(company):
    return company[2]

companies.sort(key=sort_key, reverse=True)
print(companies)

# Using the Python List sort() method to sort a list of tuples with lambda expression
companies = [('Google', 2019, 134.81), ('Apple', 2019, 260.2), ('Facebook', 2019, 70.7)]
companies.sort(key = lambda companies : companies[2])
print(companies)
