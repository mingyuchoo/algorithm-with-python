from math import sqrt


def my_function(data=None):
    return_value = None
    if data is None or \
       data > 50000000000000:
        return return_value
    square_root = sqrt(data)
    if square_root.is_integer():
        return_value = (int(sqrt(data)) + 1)**2
    else:
        return_value = -1

    return return_value
