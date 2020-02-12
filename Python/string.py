# whatever to use ' ' or " "
print('1. Usar \' ou " tanto faz, as diferenças ficarão quando usar os escapes \\')

# without print() '\n' is a string, in print() '\n' is a escape to produces new line
print('2. quebra de linha\ndentro do método print funciona')

# use 'r' before string to use raw string (without escapes)
print(r'3. c:\user\mateus\newline')

# to use multiple lines in string, only using triple-quotles """...""" or '''...'''
# use '\' to show text in same line
print('''4.
test with multiple line string
new line \
test''')

# concat string with '+' and repeat a string with '*'
print('ba' + 'na' * 2)

# two or more string literals (with same quotes) next to each other are automatically concatenated
# this only works with two literals though, not with variables or expressions:
print('Hell' 'o')