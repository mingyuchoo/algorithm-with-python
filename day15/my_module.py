def my_function(data1=None, data2=None):
    return_value = None
    if data1 is None or data2 is None:
        return return_value
    if not isinstance(data1, list) or not isinstance(data2, list):
        return return_value

    return return_value
