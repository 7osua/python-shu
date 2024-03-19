
'''
link : https://www.pythontutorial.net/python-basics/python-string/
---------------------------------------------------------------------
Learn about Python string and its basic operations.
'''

message = 'this is a string in python'
print(message)
message = "this is also a string"
print(message)
message = "it's a string"
print(message)
message = '"beautiful is better than ugly.". said Tim Peters'
print(message)
message = 'It\'s also a valid string' # using \ as escape an character
print(message)
message = r'C:\python\bin' # 'r' means raw string
print(message)

# multiline strings
help_message = ''' 
Usage : mysql command
    -h hostname
    -d database name
    -u username
    -p password
'''
print(help_message)

name = 'john'
greetText = f'hello {name}' # f-string, embed variables value inside a string
print(greetText)

greetText = 'Good ' "morning" # string concatenating
print(greetText)

greetText = greetText + f" {name}" # concatenating with variables
print(greetText)

print(greetText[5]) # accessing string element with []
print(greetText[-4:]) # accessing with negative base indexed
print(greetText[0:5]) # accessing range of a string or slicing a string
greetText = greetText[5:];
'''
greetText[0] = 'M' # String are immutable, cannot change. Except assigned as new value
'''
print(greetText)
print(len(greetText))
newText = 'Afternoon ' + greetText[8:]
print(newText)
