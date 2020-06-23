import time


def solution(priorities: list, location: int) -> int:
    answer = 0

    queue = [[i, v] for i, v in enumerate(priorities)]

    max_value = max(priorities)
    max_index = priorities.index(max_value)

    print(queue)
    for i in range(max_index):
        task = queue.pop(0)
        queue.append(task)
        print(queue)
        time.sleep(1)
    print(queue)
    answer = [i for (i, v) in queue].index(location) + 1
    return answer
