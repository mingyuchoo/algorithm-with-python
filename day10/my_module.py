def my_function(data=None):
    return_value = None
    if data is None:
        return return_value
    if isinstance(data, list):
        sum_of_data = sum(data)
        len_of_data = len(data)
        return sum_of_data/len_of_data
    else:
        return return_value
