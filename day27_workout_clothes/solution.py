## 내가 푼 오답
def solution_failed(n: int, lost: list, reserve: list) -> int:
    remain = []
    # 초기화
    check_list = [1] * n

    # 도난처리1-1
    for i in lost:
        check_list[i - 1] -= 1

    # 여벌처리
    for i in reserve:
        check_list[i - 1] += 1

    # 잃어버린 학생 기준으로 처리
    while lost:
        inspect = lost.pop(0)
        if (inspect - 1 - 1) >= 0 and check_list[inspect - 1 - 1] > 1:
            check_list[inspect - 1 - 1] -= 1
            check_list[inspect - 1] += 1
        elif inspect <= (n - 1) and check_list[inspect] > 1:
            check_list[inspect] -= 1
            check_list[inspect - 1] += 1
        else:
            remain.append(inspect)
    answer = n - len(remain)
    return answer


## 남이 푼 정답
def solution(n: int, lost: list, reserve: list) -> int:
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    # 여벌이 있는 학생 기준으로 처리
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)
