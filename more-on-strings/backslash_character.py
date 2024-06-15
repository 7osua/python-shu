# link : https://www.pythontutorial.net/python-basics/python-backslash/

# Introduction to the '\' characters.

text = "Hello\nWorld!"
another_text = "Some\ttext"
example_text = '"Python\'s awesome" she said.'
print(len("\n"))
print(text)
print(another_text)
print(example_text)

# In python, the backslash '\' is a special character.
# If we use the '\' backslash it can changes the meaning of that character.
# Example, the 't' character is a literal character.
# If we use the '\' character in front of the letter 't',
# it will become the tab character '\t'.

"""
Generally, the backslash has two main purposes.
1. The backslash character is a part of special character
   sequences such as the tab character \\t or the new line character \\n.
2. The backslash (\\) escape other special characters.
   For example, if you have a string that has
   a single quote inside a single-quoted string like the following string.
"""

# The '\' backslash in F-strings

# colors = ["red", "green", "blue"]
# rgb_text = f"the RGB colors are:\n{'\t'.join(colors)}" # SyntaxError
# print(rgb_text)

"""
To fix this, you need to join the strings in the colors list
before placing them in the curly braces:
"""

colors = ["red", "green", "blue"]
rgb = "\n".join(colors)
rgb_text = f"the RGB colors are:\n{rgb}"
print(rgb_text)

# PEP-498  specifies that an f-string cannot contain a baclslash character
# as par of the expression inside the curly braces {}.


# The '\' backslash in raw strings.

yet_another_text = r"\n"
print(yet_another_text)
print(f"yet_another_text length is : {len(yet_another_text)}")

# The raw-strings treat the backslash (\) as literal character.


"""
Lear about the backslash character "\\" as a part of a special sequence
character or to escape characters in a string.

summary:
1. The python backslash character is a special character
   used as part of a special sequence such as
   tab character and new line character.
2. Use the backslash character to escape other special character
   for example the using to escape singele quote within string literal with
   single quote.
3. the f-string cannot contain the backslash as a part of expression inside
   the curly braces {}.
4. Raw string treat the backslash as a literal character.
"""
