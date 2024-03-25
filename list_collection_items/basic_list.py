'''
link : https://www.pythontutorial.net/python-basics/python-list/
-----------------------------------------------------------------
Learn about Python List type and how to manipulate list elements effectively.
- Use square bracket notation [] to access a list element by its index. The first element has an index 0.
- Use a negative index to access a list element from the end of a list. The last element has an index -1.
- Use list[index] = new_value to modify an element from a list.
- Use append() to add a new element to the end of a list.
- Use insert() to add a new element at a position in a list.
- Use pop() to remove an element from a list and return that element.
- Use remove() to remove an element from a list.
'''

# A list is an ordered collection of items, python uses "[]" to indicate a list.
todo_list = ['Learn python', 'Learn JavaScript', 'Learn TypeScript', 'Learn SQL', 'Learn NoSQL']
print(todo_list)

colors = ['Orange', 'Toska', 'Blue Sky', 'Yellow', 'Blue Army']
print(colors)

coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)

# Accessing elements in a list
numbers = [1, 3, 2, 7, 9, 4]
print(numbers[0])
print(numbers[0:3])
print(numbers[-1])
print(numbers[-2])
print(numbers[-3:-1])

# Modifiying, adding and removing elements
numbers[0] = 10
print(numbers)

numbers[1] = numbers[1] * 10
print(numbers)

numbers[2] /= 2
print(numbers)

# Adding elements to the list
numbers.append(100)
print(numbers)

numbers.insert(2, 200)
print(numbers)


# Removing elements from a list
# Remove element by position.
del numbers[2]
print(numbers)

last = numbers.pop()
print(f'numbers = {numbers} | last = {last}')

second = numbers.pop(2)
print(f'numbers = {numbers}')

# Remove element by value, use 'remove()'.
numbers = [1, 3, 7, 2, 9, 4, 9]
print(numbers)
numbers.remove(9)
print(numbers)

