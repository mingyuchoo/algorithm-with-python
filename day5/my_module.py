def my_function(data=None):
    return_value: str = ""
    if data is None or data == "":
        return return_value
    position = len(data) // 2
    if len(data) % 2 == 0:
        return_value = data[position - 1: position + 1]
    else:
        return_value = data[position]
    return return_value
