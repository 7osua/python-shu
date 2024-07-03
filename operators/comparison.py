# link : https://www.pythontutorial.net/python-basics/python-comparison-operators/

# Introduction to the comparison operators

"""
In programming, you often want to comapare a value with another value.
To do that, you use comparison operators.

Python has six comparison operators, which are as follows:

- '<'   => Less than
- '>='  => Less than or equal to
- '>'   => Greater than
- '>='  => Greater than or equat to
- '=='  => Equal to
- '!='  => Not Equal to

These comparison operators compare two values and
return a boolean value, either 'True' or 'False'.

You can use these comparison operators to compare both
numbers and strings.
"""

# Less than operator '<'

"""
The Less Than operator '<' compares two values and returns 'True'
if the value on the left is less than the value on the right.
Otherwise, it returns 'False'.

    left_value < right_value

The following example uses the Less Than '<' operator
to compare two numbers.
"""

x = 10
y = 20

print(f"x < y ? {x < y}")
# [Output] x < y ? True

print(f"y < x ? {y < x}")
# [Output] x < y ? False

print("'apple' < 'banana' = ", "apple" < "banana")
# [Output] 'apple' < 'banana' =  True

print("'banana' < 'apple' = ", "banana" < "apple")
# [Output] 'banana' < 'apple' =  False

"""
The expression 'apple' < 'orange' returns 'True'
because the letter a in apple is before
the letter o in orange.

Similarly, the 'banana' < 'apple' returns 'False'
because the letter 'b' is after the letter 'a'.
"""

# Less than or Equal To operator


"""
The following example shows how to use the less than or equal
to operator to compare two numbers.
"""

print(f"20 <= 20 ? {(20 <= 20)}")
# [Output] 20 <= 20 ? True

print("10 <= 20 ? ", (10 <= 20))
# [Output] 10 <= 20 ?  True

print("30 <= 29 ? ", (30 <= 29))
# [Output] 30 <= 29 ?  False


"""
This example shows how to use the less than or equal
to operator to compare the values of two variables.
"""

x = "x"
y = "y"

print(f"x <= y ? {x <= y}")
# [Output] x <= y ? True

print(f"y <= x ? {y <= x}")
# [Output] y <= x ? False

"""
The less than or equal to operator compares two values
and returns 'True' if the left value is less than or
equal to the right value. Otherwise, it returns 'False'.
"""


# Greater than operator

"""
This example uses the greater than operator '>'
to compare two numbers.
"""
print(f"20 > 10 ? {20 > 10}")
# [Output] 20 > 10 ? True

print("20 > 20 ? ", 20 > 20)
# [Output] 20 > 20 ?  False

print("10 > 20 ? ", 10 > 20)
# [Output] 10 > 20 ?  False


"""
The following example uses the greater
than operator '>' to compare two strings.
"""
print("orange > apple ? ", ("orange" > "apple"))
# [Output] orange > apple ?  True

print("apple > orange ? ", ("apple" > "orange"))
# [Output] apple > orange ?  False


"""
The greater than the operator '>' compares two values
and returns 'True' if the left value is greater than the right value.
Otherwise, it returns 'False'.
"""

# Greater than or equal to operator


"""
The following example uses the greater than or equal to an operator
to compare two numbers.
"""

print(f"20 >= 10 = {20 >= 10}")
# [Output] 20 >= 10 = True

print("20 >= 20 = ", 20 >= 20)
# [Output] 20 >= 20 =  True

print("10 >= 20 = ", 10 >= 20)
# [Output] 10 >= 20 =  False


"""
The following example uses the greater than or equal to operator
to compare two strings.
"""

print("apple >= apple = ", ("apple" >= "apple"))
# [Output] apple >= apple =  True

print("apple >= orange = ", ("apple" >= "orange"))
# [Output] apple >= orange =  False

print("orange >= apple = ", ("orange" >= "apple"))
# [Output] orange >= apple =  True


"""
The greater than or equal to operator '>=' compares two values and returns
'True' if the left value is greater than or equal to the right value.
Otherwise, it returns 'False'.
"""


# Equal to operator


"""
The following example uses the equal to operator '=='
to compare two numbers.
"""

print(f"10 == 20  ? {10 == 20}")
# [Output] 10 == 20  = False

print(f"20 == 20  ? {20 == 20}")
# [Output] 20 == 20  ? True

"""
The following example uses the equal to operator '=='
to compare two strings
"""

print("apple == apple ? ", ("apple" == "apple"))
# [Output] apple == apple ?  True

print("apple == orange ? ", ("apple" == "orange"))
# [Output] apple == orange ?  False

"""
The equal to operator '==' compares two values and returns
'True' if the left value is equal to the right value.
Otherwise, it returns 'False'.
"""


# Not Equal to operator


"""
The following uses the not equal to operator
to compare two numbers.
"""

print("20 != 20 ?", (20 != 20))
# [Output] 20 != 20 ? False

print("20 != 10 ?", (20 != 10))
# [Output] 20 != 10 ? True

"""
The following example uses the not equal to operator
to compare two strings.
"""

print("apple != apple = ", ("apple" != "apple"))
# [Output] apple != apple =  False

print("apple != orange = ", ("apple" != "orange"))
# [Output] apple != orange =  True

"""
The not equal to operator '!=' compares two values and
returns 'True' if the left value isn't equal to
the right value. Otherwise, it returns 'False'.
"""


"""
Learn about Python comparison operators and how to use them to compare two values.

[Summary]
- A comparisan operator compares two values and
  returns a boolean value, either 'True' or 'False'.
- Python has six comparison operators:
  less than '<', less than or equal to '<=',
  greater than '>', greater or equal to '>=',
  equal to '==', not equal to '!='.
"""
