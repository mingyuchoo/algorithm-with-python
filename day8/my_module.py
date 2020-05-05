def my_function(x=None, n=None):
    return_value = None
    if x is None or \
       x < -10000000 or \
       x > 10000000 or \
       n is None or \
       n < 0 or \
       n > 1000:
        return return_value
    if x > 0:
        return_value = list(range(x, x*n+1, x))
    elif x == 0:
        return return_value
    else:
        return_value = list(range(x, x*n-1, x))
    return return_value
