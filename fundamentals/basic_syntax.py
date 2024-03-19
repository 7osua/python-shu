import keyword


# define main() function to print something.
def main():
    print("""hello, this is basic syntax""")


# call main function
main()

a = True
b = True
c = True

if (a and b) and \
        (c or a):
    print(f"a : {a}, b : {b}, c : {c}")


s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = '''
string can span
multiple line
'''
print(s)

print(keyword.kwlist)
