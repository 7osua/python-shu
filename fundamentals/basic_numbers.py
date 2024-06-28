"""
link : https://www.pythontutorial.net/python-basics/python-numbers/
"""

# Integers

sum = 20 + 10
print(sum)
# [Output] 30

sub = 20 - 10
print(sub)
# [Output] 10

mul = 20 * 10
print(mul)
# [Output] 200

div = 20 / 10
print(div)
# [Output] 2.0

exp = 3**3  # Calculate exponents with '**'
print(exp)  # With two multiplication symbols
# [Output] 27

ord = 20 / (10 + 10)  # Order of operations, with the '()' parantheses.
print(ord)
# [Output] 1.0

"""
The integers are number such as -1, 0, 1, 2, and 3, ...
and they have type 'int'.

You can use Math operator like '+', '-', '*', and '/'
to form expressions that include integers.
"""

# Floats

"""
Any number with decimal point '.' is a floating-point number.
The term float means that decimal point can appear at any
posisiton in a number.

In general we can use float like intergers.
"""

print(0.5 + 0.5)
# [Output] 1.0

print(0.5 - 0.5)
# [Output] 0.0

print(0.5 * 0.5)
# [Output] 0.25


print(0.5 / 0.5)  # division always return a float
# [Output]

"""
If you mix an integer and a float in any arithmetic operation,
the result is a float.
"""
print(1 + 2.0)
# [Output] 3.0


"""
[Note]
Due to the internal representation of floats, Python will try to
represent the result as precisely as possible. However, you may
get the result that you would not expect.

Just keep this in mind when you perform calculations with floats.
"""
print(0.1 + 0.2)
# [Output] 0.30000000000000004


# Underscores in numbers

"""
When a number is large,  it'll becoame difficult to read.

    count = 10000000000

To make the long numbers more readable, you can group digits
using underscores.
The underscores also work for both the integers and floats.
"""
count = 10_000_000_000
print(count)
# [Output] 10000000000

tax = 1.2_000_10090
print(tax)
# [Output] 1.200010090

"""
Learn about Python numbers and how to use them in programs.

[Summary]

- Python supports common numeric types including
  intergers, floats, and complex numbers.
- Use the underscores to group numbers for the large
  numbers.
"""
