def my_function(a=None, b=None):
    return_value = None
    if a is None or b is None:
        return return_value
    if not isinstance(a , list) or not isinstance(b, list):
        return return_value
    if a == [] or b == []:
        return return_value

    result_list = []
    for i, j in zip(a, b):
        temp = []
        for x, y in zip(i, j):
            temp.append((x +y))
        result_list.append(temp)
    return_value = result_list
    return return_value
