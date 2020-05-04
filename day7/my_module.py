def my_function(data=None):
    return_value = ''
    if data is None or data == '':
        return return_value
    data_list = data.split(' ')
    new_list = []
    for item in data_list:
        new_word = []
        for index in range(len(item)):
            if index % 2 == 0:
                new_word.append(item[index].upper())
            else:
                new_word.append(item[index].lower())
        new_list.append(''.join(new_word))

    return_value = ' '.join(new_list)
    return return_value
