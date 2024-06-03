# link : learn various way to write text files in python.
"""
Summary

- Use the open() function with the w or a mode to open a text file for appending.
- Always close the file after completing writing using the close() method or use the with statement when opening the file.
- Use write() and writelines() methods to write to a text file.
- Pass the encoding='utf-8' to the open() function to write UTF-8 characters into a file.
"""


# Steps for writing to text files
"""
To write to a text file in Python, you follow these steps:

- First, open the text file for writing (or append) using the open() function.
- Second, write to the text file using the write() or writelines() method.
- Third, close the file using the close() method.

The open() function accepts many parameters. But you’ll focus on the first two:

    f = open("file", "mode")
    
- The "file" parameter specifies the path to the text file that you want to open for writing.
- The "mode" parameter specifies the mode for which you want to open the text file.

For writing to a text file, you use one of the following modes:

Mode	Description
'w'	    Open a text file for writing. If the file exists, 
        the function will truncate all the contents as soon as you open it. 
        If the file doesn’t exist, the function creates a new file.
'a'	    Open a text file for appending text. If the file exists, the function append contents at the end of the file.
‘+’	    Open a text file for updating (both reading & writing).

The open() function returns a file object that has two useful methods for writing text to the file:
.write() and .writelines().

- The write() method writes a string to a text file.
- The writelines() method write a list of strings to a file at once.
"""


# Writing text files
file_name = "learn_material.txt"
text_content = ["Learn python", "Learn SQL", "Learn Spark", "Learn SQLite", "Learn Matplotlib", "Learn Pandas"]
with open(f'files\\{file_name}', 'w') as file:
    for line in text_content:
        file.writelines(line)
        file.writelines("\n")


# Appending text files
add_text_content = ["Learn Flask", "Learn Jinja", "Learn Airflow"]
with open(f'files\\{file_name}', 'a') as file:
    for line in add_text_content:
        file.write(line)
        file.write('\n')


# Writing to a UTF-8 text file
quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'
with open(f'files\\{file_name}', encoding='utf-8', mode='a') as file:
    file.write(quote)
    file.write('\n')
    # UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-44: character maps to <undefined>
    # To open a file and write UTF-8 characters to a file,
    # you need to pass the encoding='utf-8' parameter to the open() function.
