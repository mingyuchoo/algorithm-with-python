def solution(participant=None, completion=None):
    answer = ''
    if not isinstance(participant, list) or not isinstance(completion, list):
        return answer
    participant.sort()
    completion.sort()

    for i, j in zip(participant, completion):
        if i != j:
            return i
    answer = participant[-1]

    return answer
