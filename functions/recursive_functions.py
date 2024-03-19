'''
link : https://www.pythontutorial.net/python-basics/python-recursive-functions/
--------------------------------------------------------------------------------
A recursive function is a function that calls itself until it doesn’t.
And a recursive function always has a condition that stops calling itself.
'''


# a countdown function that counts down from a specified number to zero.
def count_down(start):
    """
    count down from a number value is assigned from 'start' as an argument.
    call the count_down() if the next number
    is greater than 0.
    """
    print(start)

    next = start - 1
    if next > 0 :
        count_down(next)

print("COUNT DOWN : ")
count_down(3)

# calculate a sum of a sequence e.g., from 1 to 100. A simple way to do this is to use a for loop with the range() function

def sum(n):

    if n > 0:
        print(n)
        return n + sum(n-1)

    return 0

print("SUM of a sequence number end with n range() : ")
result = sum(3)
print(f"--------+\n{result}")


def sum_variant_ternary_operator(n):
    print(n)
    return n + sum_variant_ternary_operator(n-1) if n > 0 else 0

print("SUM of a sequence number simplified with ternary operator")
result = sum_variant_ternary_operator(3)
print(f"--------+\n{result}")
