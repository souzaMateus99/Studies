# python for iterates over the items of any sequence (without halting condition)
words = ['cat', 'dog', 'bird', 'butterfly']
for animal in words:
    print(animal)

# if you need iterate over a sequence of numbers, use range() method
for i in range(10):
    print(i)

# example using range with len, to iterate with list count
names = ['Mateus', 'Joao', 'Zequinha']
for i in range(len(names)):
    print(i, names[i])