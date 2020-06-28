def solution(prices: list) -> list:
    # 입력과 출력의 길이가 같다면 출력의 길이를 미리 정한다.
    # 비효율적인 예) answer = [0 for _ in range(len(prices))]
    length = len(prices)
    answer = [0] * length
    stack = []
    for index in range(length):
        # stack 길이는 변동되므로 변수에 할당하지 않고 그대로 이용한다.
        # stack이 다 빌 때까지 진행 -> 그러면 스택에 넣는 상황과 빼는 상황을 고려해야한다.
        while len(stack) != 0 and \
                prices[index] < prices[stack[len(stack) - 1]]: # 확인하고자하는 주식가격 prices[i]이 비교하고자하는 위치의 주식가격보다 작을 때까지
            temp = stack.pop()
            answer[temp] = index - temp
        stack.append(index)

    # 답 정리 작업
    while len(stack): # stack에 아이템이 있을 동안
        temp = stack.pop()  # stack에서 주식 위치값을 빼내서
        answer[temp] = length - temp - 1  # 전체 길이에서 값이 내려간 시점까지의 간격을 저장한다.

    return answer
