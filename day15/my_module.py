def my_function(data1=None, data2=None):
    return_value = None
    if data1 is None or data2 is None:
        return return_value
    if not isinstance(data1, list) or not isinstance(data2, list):
        return return_value

    count = len(data1)
    smallest = None
    for i in range(count):
        temp = 0
        for j in range(count):
            temp += data1[j] * data2[(j+i)%count]
        if smallest is None or smallest > temp:
            smallest = temp

    return_value = smallest

    return return_value
