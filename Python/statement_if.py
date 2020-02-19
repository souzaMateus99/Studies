num = int(input('Please enter an integer: '))

if num < 0:
    num = 0
    print('Negative changed to zero')
elif num == 0:
    print('Zero')
elif num == 1:
    print('Single')
else:
    print('More')

# 'elif' is short for 'else if'