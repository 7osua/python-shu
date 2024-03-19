'''
link : https://www.pythontutorial.net/python-basics/python-default-parameters/
-------------------------------------------------------------------------------
Learn about the Python default parameters to simplify function calls.
'''


def print_message(message, name = "john"):
    return f"{message} {name}!"

user_message = print_message("hi", "josua")
print(user_message)

user_message = print_message("olla")
print(user_message)


# Multiple default value parameters.
def greet_text(message = "Hi", name="There"):
    return f"{message} {name}!"

user_greet_text = greet_text()
print(user_greet_text)

# function expect "there" as message = "there" argument.
user_greet_text = greet_text("there")
print(user_greet_text)

user_greet_text = greet_text(name = "Jenny")
print(user_greet_text)
