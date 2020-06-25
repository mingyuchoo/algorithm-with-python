def solution(arrangement: str) -> int:
    arrangement = arrangement.replace('()', '0')
    uncut = 0
    cutted = 0
    for element in arrangement:
        if element == '(':  # 새로운 쇠막대가 놓여 있냐?
            uncut += 1
            cutted += 1
        elif element == '0': # 레이저 포인터 지졈이냐?
            cutted += uncut
        elif element == ')': # 쇠막대 끝 지점이냐?
            uncut -= 1
        else:
            pass
    return cutted
