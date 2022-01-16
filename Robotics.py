def print_numbers(until):
    for i in range(1, until + 1):
        print(i)


# for 10 times
# print_numbers(10)

# print_even_number(4) example: it should print 2,4,6,8
# def print_even_numbers(No_of_numbers):
#     for i in range(2, No_of_numbers*2+1, 2):
#         print(i)
#
# print_even_numbers(2)

def print_odd_numbers(No_of_numbers):
    for i in range(1, No_of_numbers * 2 + 1, 2):
        print(i)


# print_odd_numbers(10)

# double_every_odd_number(4) 2,2,6,4
# double_every_odd_number(6) 2,2,6,4,10,6

def double_every_odd_number(No_of_numbers):
    for i in range(1, No_of_numbers + 1):
        if i % 2 != 0:
            print(i + i, end=",")
        else:
            print(i, end=",")


# double_every_odd_number(6)

def double_every_even_number(No_of_numbers):
    for i in range(1, No_of_numbers + 1):
        if i % 2 == 0:
            print(i + i, end=",")
        else:
            print(i, end=",")


# double_every_even_number(6)
# print_factoral(5) 5X4x3x2x1= 120
# print_factoral(3) 3x2x1= 6

def factoral(No_of_numbers):
    result = 1
    for i in range(No_of_numbers, 0, -1):
        # print(i)
        result = result * i
    return result


# print(factoral(3) + factoral(2))


def factoral_recursive(number):
    if(number<=1):
        return 1
    # print(number)
    return factoral_recursive(number - 1)*factoral_recursive(number-2)


print(factoral_recursive(4))
