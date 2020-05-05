def my_function(target_list=None, range_list=None):
    return_value = []
    if target_list is None or not isinstance(target_list, list):
        return return_value
    if range_list is None or not isinstance(range_list, list):
        return return_value

    for item in range_list:
        cutter_list = target_list[item[0] - 1: item[1]]
        sorted_list = sorted(cutter_list)
        return_value.append(sorted_list[item[2] - 1])
    return return_value
