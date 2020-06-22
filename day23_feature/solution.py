def solution(progresses: list, speeds: list) -> list:
    answer = []
    while progresses:
        progresses = list(map(lambda x, y: x + y, progresses, speeds))
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count:
            answer.append(count)
    return answer
