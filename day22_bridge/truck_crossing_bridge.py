## 시간초과 케이스 발생
# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     q = [0] * bridge_length
#
#     while q:
#         time += 1
#         q.pop(0)
#         if truck_weights:
#             if sum(q) + truck_weights[0] <= weight:
#                 q.append(truck_weights.pop(0))
#             else:
#                 q.append(0)
#
#     return time


def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge_weight = []
    on_bridge_time = []

    while truck_weights or on_bridge_weight:
        time += 1
        if on_bridge_time:
            if on_bridge_time[0] + bridge_length == time:
                on_bridge_weight.pop(0)
                on_bridge_time.pop(0)
        if truck_weights:
            if sum(on_bridge_weight) + truck_weights[0] <= weight:
                on_bridge_weight.append(truck_weights.pop(0))
                on_bridge_time.append(time)

    return time


if __name__ == "__main__":
    print(8 == solution(2, 10, [7, 4, 5, 6]))
    print(101 == solution(100, 100, [10]))
    print(110 == solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
