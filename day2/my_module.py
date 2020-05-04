import re


def my_function(input_data=None):
    if input_data is None or input_data == "":
        return False
    if len(str(input_data)) <= 3 or len(str(input_data)) >= 9:
        return False
    if re.search("^[0-9]+$", str(input_data)) is None:
        return False
    else:
        return True
