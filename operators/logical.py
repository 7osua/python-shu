"""
link : https://www.pythontutorial.net/python-basics/python-logical-operators/
"""

# Introduction to logical operators

"""
Sometimes, you may want to check multiple conditions at
the same time. To do so, you use logical operators.

Python has three logical operators :
- 'and'
- 'or'
- 'not'
"""


# The "and" operator

"""
The 'and' operator check whether two conditions are
both 'True' simultaneously.

    a and b

It return 'True' if both conditions are 'True'.
And it returns 'False' if either the condition
'a' and 'b' is 'False'.

The following table illustrates the result of
the 'and' operator when combining two conditions:

a = True	| and  | b = True	=> True
a = True	| and  | b = False	=> False
a = False	| and  | b = False	=> False
a = False	| and  | b = True	=> False

As you can see, the condition 'a' and 'b'
only returns 'True' if both conditions evaluate
to 'True'.
"""

price = 9.99

print(f"price > 9 and price < 10 = {price > 9 and price < 10}")
# [Output] price > 9 and price < 10 = True

print(f"price > 10 and price < 20 = {price > 10 and price < 20}")
# [Output] price > 10 and price < 20 = False

"""
In the examples above, the 'and' operator used to
combine two conditions that compare the 'price' with numbers.
The result is 'True' because the 'price' is
greater than 9 and less than 10.

Then, the next conditions will returns 'False' because the 'price'
isn't greater than 10. The condition 'price > 10' returns 'False'
while the second condition 'price < 20' returns 'True'.
"""

# The "or" operator

"""
Similiar to the 'and' operator, the 'or' operator checks
multiple conditions. But returns 'True' when either or
both individual conditions are 'True'.

    a or b

The following table illustrates the result of the 'or' operator
when combining two conditions

a = True	| or  | b = True	=> True
a = True	| or  | b = False	=> True
a = False	| or  | b = True	=> True
a = False	| or  | b = False	=> False


The 'or' operator returns 'False' only when both
conditions are 'False'.
"""

print(f"price > 10 or price < 20 = {price > 10 or price < 20}")
# [Output] price > 10 or price < 20 = True

print(f"price > 10 or price < 5 = {price > 10 or price < 5}")
# [Output] price > 10 or price < 5 = False

"""
In the exaples above, the conditions will returns 'True'.
because the first condition 'price > 10' is 'False' but
the second condition is 'True' because the 'price < 20', which
will return 'True' because one of the conditions is 'True'.

Then, the next condition will return 'False' because both conditions
evaluate to 'False'.
"""


# The "not" operator

"""
The 'not' operator applies to one condition. It reverses the result
of that condition, 'True' becomes 'False' and 'False' becomes 'True'.

    not a

if the conditions is 'True', the 'not' operator returns 'False'
and vice cersa.

not  | a = True	    => False
not  | a = False	=> True

The following table illustrates the result of the not operator.
"""

price = 9.99
print(f"not price > 10 = {not price > 10}")
# [Output] not price > 10 = True

print(f"not price < 10 = {not price < 10}")
# [Output] not price < 10 = False

# Combine logical operators
print(f"not (price > 5 and price < 10) = {not (price > 5 and price < 10)}")
# [Output] not (price > 5 and price < 10) = False


"""
The examples above uses the 'not' operator.
Since the 'price > 10' returns 'False',
the not 'price > 10' returns 'True'.

Then, the next examples that combines the 'not' operator
and the 'and' operator.
Python evaluates the conditions based on the following order:

- First, 'price > 5 and price < 10' evaluates to 'True'.
- Second, 'not True' evaluates to 'False'.

This leads to an important concept called precedence of logical operators.
"""


# Precedence of Logical Operators

"""
When you mix the logical operators in an expression,
python will evaluate them in the order which is called
the operator precedence.

The following shows the precedence of the 'not', 'and',
'or' operators.

Operator    =>  Precedence
not 	    =>  High
and	        =>  Medium
or	        =>  Low

Based on these precedences, Python will group
the operands for the operator with the highest precedence first,
then group the operands for the operator with
the lower precedence, and so on.

In case an expression has several logical operators with
the same precedence, Python will evaluate them from the left to right.

a or b and c	    =>  	a or (b and c)
a and b or c and d	=>  	(a and b) or (c and d)
a and b and c or d	=>  	((a and b) and c) or d
not a and b or c	=>  	((not a) and b) or c
"""


"""
Learn about Python logical operators and
how to use them to combine multiple conditions.

[Summary]

- Use logical operator to combine multiple conditions.
- Python has three logical operators:
  'not', 'and', 'or'.
  The precedence of the logical operator from the higest
  to the lowest :
  'not' => 'and' => 'or'.
"""
