def my_function(data=None, counter=None):
    return_value = None
    if data is None or counter is None:
        return return_value
    if not isinstance(data, str) or not isinstance(counter, int):
        return return_value

    for j in range(counter):
        storage = []
        for i in range(len(data)):
            storage.append(data[:i] + data[i+1:])
        storage.sort(reverse=True)
        data = storage[0]

        return_value = int(data)
    return return_value
