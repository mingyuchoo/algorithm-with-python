def solution(h):
    a = [0] * len(h)
    for i in range(len(h) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if h[j] > h[i]:
                a[i] = j + 1
                break
    return a


if __name__ == "__main__":
    print(solution([6, 9, 5, 7, 4]))
    print(solution([3, 9, 9, 3, 5, 7, 2]))
    print(solution([1, 5, 3, 6, 7, 6, 5]))
