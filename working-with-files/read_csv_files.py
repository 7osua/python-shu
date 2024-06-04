# link : https://www.pythontutorial.net/python-basics/python-read-csv-file/


"""
Learn how to read a CSV file in Python using the built-in csv module.

What is CSV file ?

- CSV stands for Comma-Seperated Values.
- A CSV is a delimited text file that use comma "," to separate values.
- A CSV files consist of one or more lines. Each line is a data record.
  Each data record consist one or more values separated by commas.
- In addition, all the lines of a ".csv" file have the same number of values.
- A CSV file typically used to store tabular data in plain text.

- Use csv.reader() function or csv.DictReader class to read data from a CSV file.
"""

import csv

# Introduction : reading ".csv" file

"""
1. Import the "csv" module
2. Open the ".csv" file using the built-in open() function in read mode.
3. If the ".csv" contains UTF-8 characters, specify the "encoding" argument with "utf-8".
4. Pass the "f" object to the ".reader()" function of the "csv" module.
   The ".reader()" function return a csv reader object.
5. The "csv_reader" is an iterable object of lines from the CSV file.
   Therefore, it can be iterate over the lines of the CSV file using a "for" loop.
6. Each line is a list of values. To access each value, we can use "[]" notation.
7. Close the file once you’re no longer access it by calling the close() method of the file object
   or use the "with" statement so that you don’t need to explicitly call the close() method.
   
    import csv
    with open('files/country.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line)
"""

country_file = "country.csv"
dir_path = "files"

with open(f"{dir_path}\\{country_file}", "r") as country_data:
    csv_reader = csv.reader(country_data)
    for line in csv_reader:
        print(line)

"""
The "country.csv" has the first line as the header. 
To separate the header and data, you use the "enumerate()" function to get the index of each line.
Use the "enumerate()" function and specify the index of the first line as 1.

Another way to skip the header is to use the next() function. 
The "next()" function forwards to the reader to the next line.


The following example reads the country.csv file and calculate the total areas of all countries:
"""

country_file_values = open(f"{dir_path}\\{country_file}", "r", encoding="utf-8")
another_csv_reader = csv.reader(country_file_values)
for line_no, line in enumerate(another_csv_reader, 1):
    if line_no == 1:
        print("Header")
        print(line)
        print("Row")
    else:
        print(line)
country_file_values.close()

# calculate the total area of all countries
country_file_another_values = open(f'{dir_path}\\{country_file}', 'r', encoding="utf-8")
one_more_csv_reader = csv.reader(country_file_another_values)
total_area_accumulation = 0

next(one_more_csv_reader)  # skip the first row
for no_line, line in enumerate(one_more_csv_reader, 1):
    total_area_accumulation += float(line[1])  # calculate total

country_file_another_values.close()
print(f'total_area_accumulation : {total_area_accumulation}')

# Reading a CSV file using the "DictReader" class

"""
When you use the csv.reader() function, 
you can access values of the CSV file using the bracket notation such as line[0], line[1], and so on. 
However, using the csv.reader() function has two main limitations:

- First, the way to access the values from the CSV file is not so obvious. 
  For example, the line[0] implicitly means the "country name". 
  It would be more expressive if you can access the country name like line['country_name'].
- Second, when the order of columns from the CSV file is changed or new columns are added, 
  you need to modify the code to get the right data.

This is where the DictReader class comes into play. 
The DictReader class also comes from the csv module.

The DictReader class allows you to create an object like a regular CSV reader. 
But it maps the information of each line to a dictionary (dict) whose keys are specified 
by the values of the first line.

By using the DictReader class, you can access values in the country.csv file like 
line['name'], line['area'], line['country_code2'], and line['country_code3'].

The following example uses the DictReader class to read the country.csv file:
"""

with open(f'{dir_path}\\{country_file}', mode='r', encoding='utf-8') as file_with_dict_reader:
    csv_reader_with_dict_reader = csv.DictReader(file_with_dict_reader)

    # skip the header
    next(csv_reader_with_dict_reader)

    # show the data
    for line in csv_reader_with_dict_reader:
        print(f"The area of {line['name']} is {line['area']} km2.")

# If you want to have different field names other than the ones specified in the first line,
# you can explicitly specify them by passing a list of field names to the DictReader() constructor
# like this :

fields_name = ["country_name", "area", "code2", "code3"]  # DictReader constructor

with open(f'{dir_path}\\{country_file}', 'r', encoding='utf-8') as another_file_with_dict_reader:
    another_csv_reader_dict_reader = csv.DictReader(another_file_with_dict_reader, fields_name)
    next(another_csv_reader_dict_reader)
    for line in another_csv_reader_dict_reader:
        print(f'The code of {line["country_name"]} is {line["code2"]}.')
