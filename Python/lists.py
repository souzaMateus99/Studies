values = [104, 30, 86, 77]
increment_values = [1, 5, 10]

# return the value in indicate index
print(values[0])

# when the index is negative, the count is done backwards  
# [104, 30, 86, 77]
#    0,  1,  2   3
#   -4, -3, -2, -1
print(values[-1])

# the operator ':' return (create new list) the values between the index passed
# if has only one index (0:), it will return (create new list) all values until the end or from begin (:0)
print(values[0:3])

# the operator '+' it will create a new list with the values of both list
print(values + increment_values)

values[2] = 8
print(values)

# the append() method add a new value in list
values.append(271)
print(values)

# lists can has other lists inside
new_values = [['a', 'b', 'c'],[1, 2, 3]]
print(new_values[0])
print(new_values[0][1])