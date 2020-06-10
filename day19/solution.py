def solution(n: int) -> int:
    result: int = 0
    while True:
        result += 1
        if n == 1:
            return result
        if n % 2 == 1:
            n = n * 3 + 1
        else:
            n = n / 2


def driver(param: list) -> int:
    max_cycle_length: int = 0
    for item in range(param[0], param[1]+1):
        ret_value: int = solution(item)
        if ret_value > max_cycle_length:
            max_cycle_length = ret_value
    return max_cycle_length
