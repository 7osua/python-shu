'''
link : https://www.pythontutorial.net/python-basics/python-for-range/
---------------------------------------------------------------------
Learn about the Python for loop and how to use it to execute a code block a fixed number of times.
'''
for index in range(5) :
    print(index)



# Specifying the start value for the sequence
print('Specifying the start value for the sequence.')
for index in range(2,6) :
    print(index)


# Specifying the increment for the sequence
print('Specifying the increment for the sequence.')
for index in range(1,11,3) :
    print(index)

# excample : show odd number with range specified with increment
print('Excample : show odd number with range specified with increment')
for index in range(0,11,2) :
    print(index)


# excample : Calculate the sum of a sequence.
print('excample : Calculate the sum of a sequence.')
sum = 0
for index in range(6) :
    print(index)
    sum += index

print(sum)

n = 5
sum = 0
sum = n * (n+1) / 2
print(int(sum))
