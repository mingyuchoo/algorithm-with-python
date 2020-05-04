from functools import reduce


def sum_divisor(data_list=None):
    if data_list is None:
        raise TypeError("Parameter data_list is None.")
    else:
        return reduce(lambda a, b: a + b, data_list)


def find_divisor(num=None):
    if num is None:
        raise TypeError("Parameter num is None.")
    return [i for i in range(1, num + 1) if num % i == 0]


def my_function(num=None):
    try:
        if num is None:
            raise TypeError
        return sum_divisor(find_divisor(num))
    except TypeError:
        return -1
