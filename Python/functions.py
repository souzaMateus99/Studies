def fibonacci(number):
    a, b = 0, 1

    while a < number:
        print(a, end=' ')
        a, b = b, (a + b)
    print()

def fibonacci_2(number):
    a, b = 0, 1
    result = []

    while a < number:
        result.append(a)
        a, b = b, (a + b)
        
    return result


fibonacci(2000)
print(fibonacci_2(2000))