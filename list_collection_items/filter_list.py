'''
link : https://www.pythontutorial.net/python-basics/python-filter-list/
-----------------------------------------------------------------------
Learn how to filter list elements by using the built-in Python filter() function.
- Use the Python filter() function to filter a list (or a tuple).
'''

# Introduction to filter() function

'''Sometimes, you need to iterate over elements of a list and select some of them based on specified criteria.'''
'''Get all elements from the scores list where each element is greater than or equal to 70,'''

scores = [70, 60, 80, 90, 50]

filtered = []

for score in scores:
    if (score >= 70):
        filtered.append(score)

print(scores)
print(filtered)

'''
The filter() function iterates over the elements of the list and applies the fn() function to each element.
It returns an iterator for the elements where the fn() returns True.
'''
filtered = list(filter(lambda score: score >= 70, scores))
print(filtered)


filtered = filter(lambda score: score >= 70, scores)
filtered_iterator = []

for filtered_item in filtered:
    filtered_iterator.append(filtered_item)

print(filtered_iterator)

# Using the filter() funtion to filter a list of tuples

'''
Each element in a list is a tuple that contains the country’s name and population.
Get all the countries whose populations are greater than 300 million, you can use the filter() function
'''
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

filtered_countries = filter(lambda countries: countries[1] > 300_000_000, countries)
print(countries)
print(list(filtered_countries))
