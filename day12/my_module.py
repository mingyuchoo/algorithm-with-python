def masking_string(a=None, b=None):
    return_value = None
    if a is None or b is None:
        return return_value
    if not isinstance(a, str) or not isinstance(b, str):
        return return_value
    if len(a) != len(b):
        return return_value

    masked_string = []
    for i, j in zip(a, b):
        if i == '0' and j == '0':
            masked_string.append(' ')
        else:
            masked_string.append('#')
    return_value = ''.join(masked_string)

    return return_value


def convert_binary(size=None, num=None):
    return_value = -1
    if size is None or num is None:
        return return_value

    binary_string = bin(num)[0] + bin(num)[2:]
    if len(binary_string) > size:
        return_value = binary_string[1:]
    else:
        return_value = binary_string.zfill(size)
    return return_value


def my_function(n=None, data1=None, data2=None):
    return_value = []
    if n is None or data1 is None or data2 is None:
        return return_value
    if n < 0 or n > 16 or data1 == [] or data2 == []:
        return return_value
    if n != len(data1) or n != len(data2):
        return return_value

    for first, second in zip(data1, data2):
        bin_first = convert_binary(n, first)
        bin_second = convert_binary(n, second)
        return_value.append(masking_string(bin_first, bin_second))

    return return_value
