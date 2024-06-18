# link : https://www.pythontutorial.net/getting-started/python-hello-world/


def greetings():
    print("Ola\nAmigos")


def main():
    greet_text = "Hello world"
    print(f"{greet_text}")
    greetings()


main()


# Creating a new project
# 1. First, create a new directory called 'helloworld' anywhere in
#    in our system, for example : D:/helloworld
# 2. Second, launch the VS code and open the 'helloworld' directory.
# 3. Third, create a new 'app.py' file.

"""
The 'print(...)' is a built-in function that displays a message
on the screen. In this examples, it will show the message

[shell]
python app.py

[Output]
Hello world
Ola
Amigos
"""

# What is a function
"""
In general, a function takes inputs, applies some rules, and
return a result.
For examples, when we sum two numbers or when we multiply
two numbers and those functions return a new result as
a return after we apply some calculation.

In this example we already created and define two functions.
The 'greetings()' and the 'main()' functions.

Within the 'main()' function we call the 'greetings()' function.
Those two function used to print some message to the prompt shell
after we execute the 'app.py'.
"""
