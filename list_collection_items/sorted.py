'''
link : https://www.pythontutorial.net/python-basics/python-sorted/
------------------------------------------------------------------
Learn how to use the Python sorted() function to sort a list.
The sort() method sorts a list in place. In other words, it changes the order of elements in the original list.
To return the new sorted list from the original list, you use the sorted() function.
'''

# Intro sorted() function
guests = ["James", "Marry", "John", "Patricia", "Robert", "Jennifer"]
print(guests)

sorted_guests = sorted(guests, reverse = True)
print(sorted_guests)


# Using sorted() function to sort list of a numbers
scores = [5, 7, 4, 6, 9, 8]
sorted_scores = sorted(scores)
reverse_sorted_scores = sorted(scores, reverse=True)

print(scores)
print(sorted_scores)
print(reverse_sorted_scores)
