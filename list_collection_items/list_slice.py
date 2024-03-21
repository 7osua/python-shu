'''
link : https://www.pythontutorial.net/python-basics/python-list-slice/
----------------------------------------------------------------------
Learn about Python list slice and how to use it to manipulate lists effectively.
Lists support the slice notation that allows us to get a sublist from a list.
In addition to extracting a sublist, you can use the list slice to change the list such as updating, resizing, and deleting a part of the list.

a_list[begin:end:step]

Use a list slice to extract a sublist from a list and modify the list.
'''

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
sub_colors = colors[1:4]

print(colors)
print(sub_colors)


# Using list slice to get the n-first elements from a list
n_first_colors = colors[:3] # equivalent to = colors[0:3]
print(n_first_colors)

# Using list slice to get the n-last elements from a list
n_last_colors = colors[-3:]
print(n_last_colors)

# Using list slice to get every nth element from a list
nth_colors = colors[::2]
print(nth_colors)

# Using List slice to reverse a list
reverse_colors = colors[::-1]
print(reverse_colors)

# Using List slice to subtitute part of a list
subtitute_colors = colors[::1]
subtitute_colors[0:2] = ["black", "white"]
print(subtitute_colors)

# Using List slice to partially replaze and resize a list
changed_colors = colors[::1]
print(f"the list has {len(changed_colors)} elements.")
changed_colors[0:2] = ["black", "white", "gray"]
print(changed_colors)
print(f"the list has {len(changed_colors)} elements.")


# Using list slice to delete elements
deleted_colors = colors[0:]
print(deleted_colors)

del deleted_colors[2:5]
print(deleted_colors)