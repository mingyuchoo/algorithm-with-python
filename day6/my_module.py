def my_function(phone_number=None):
    return_value: str = ""
    if phone_number is None or phone_number == "":
        return return_value
    length_phone_number = len(phone_number)
    return "".join(['*'* (length_phone_number -4), phone_number[-4:]])
