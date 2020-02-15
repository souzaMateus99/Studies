# I declared variables in one line (multiple assignment)
# the values will be added in the same declaration order
# a=0, b=1
a, b = 0, 1

# the print() method will print the value of variables
print('a:', a)
print('b:', b)

while a < 100:
    # the 'end' parameter will allocate the received value to the end of printing
    print(a, end = ', ')
    a, b = b, (a + b)