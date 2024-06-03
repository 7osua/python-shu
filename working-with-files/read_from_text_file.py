# link : https://www.pythontutorial.net/python-basics/python-read-text-file/

"""
summary:
- Use the open() function with the 'r' mode to open a text file for reading.
- Use the read(), readline(), or readlines() method to read a text file.
- Always close a file after completing reading it using the close() method or the "with" statement.
- Use the encoding='utf-8' to read the UTF-8 text file.
"""

"""
Learn various way to read text files in python.
Steps for reading a text file in Python
To read a text file in Python, you follow these steps:

- First, open a text file for reading by using the open() function.
- Second, read text from the text file using the file read(), readline(), or readlines() method of the file object.
- Third, close the file using the file close() method.
"""

# open() function

"""
open() function has many parameters, we will  focusing on the first two.
open('path_to_file', 'mode')

- 'path_to_file' is a paramter with value specifies the path to text file.
- If the program and file are in the same folder, you need to specify only the filename of the file.
  Otherwise, you need to include the path to the file as well as the filename.

- The 'mode' is an optional parameter.
- It’s a string that specifies the 'mode' in which you want to open the file.
  The following table shows available modes for opening a text file:

Mode	Description
'r'	    Open for text file for reading text
'w'	    Open a text file for writing text
'a'	    Open a text file for appending text
"""
a_file = open("files\\readme.txt", "r")
content_read_lines = a_file.readlines()
print(f"content_read_lines :\n{content_read_lines}")
a_file.close()

# reading text methods
"""
The file object provides you with three methods for reading text from a text file:

- .read() read some contents of a file based on the optional size and return the contents as a string.
  If you omit the size, the read() method reads from where it left off till the end of the file.
  If the end of a file has been reached, the read() method returns an empty string.
- .readline() read a single line from a text file and return the line as a string.
  If the end of a file has been reached, the readline() returns an empty string.
- .readlines() – read all the lines of the text file into a list of strings.
  This method is useful if you have a small file and you want to manipulate the whole text of that file.
"""

# close() method
"""
The file that you open will remain open until you close it using the close() method.
To close the file automatically without calling the close() method, you use the "with" statement like this:
"""

with open("files\\readme.txt") as another_file:
    another_contents = another_file.read()
    print(f"another_contents : \n{another_contents}")

# Example reading a text file

with open("files\\readme.txt") as yet_another_file:
    print("yet_another_file :")
    for line in yet_another_file.readlines():
        print(line.strip())

with open("files\\readme.txt") as another_try_read_file:
    print("another_try_read_file :")
    [print(line.strip()) for line in another_try_read_file]

with open("files\\readme.txt") as try_read_file:
    print("try_read_file :")
    while True:
        line = try_read_file.readline()
        if not line:
            break
        print(line.strip())


# A more concise way to read a text file line by line
with open("files\\readme.txt") as text_file_to_read:
    print("text_file_to_read")
    for line in text_file_to_read:
        print(line.strip())


# Read UTF-8 text files

"""
The code in the previous examples works fine with ASCII text files.
However, if you’re dealing with other languages such as Japanese, Chinese, and Korean,
the text file is not a simple ASCII text file.
And it’s likely a UTF-8 file that uses more than just the standard ASCII text characters.

To open a UTF-8 text file, you need to pass the encoding='utf-8' to the open() function
to instruct it to expect UTF-8 characters from the file.
"""
with open("files\\quotes.txt", encoding="utf-8") as read_file_with_japanese_text:
    print("read_file_with_japanese_text : ")
    [print(line.strip()) for line in read_file_with_japanese_text.readlines()]
