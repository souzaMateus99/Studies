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


# fibonacci(2000)
# print(fibonacci_2(2000))


def default_values(text_print = "I'm default value"):
    print(text_print)


# default_values()
# default_values('Hello world!')


num = 20

def get_number(i = num):
    print(i)

num = 8

get_number()
get_number(num)