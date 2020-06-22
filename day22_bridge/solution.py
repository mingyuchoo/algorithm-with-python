def solution(bridge_length, weight, truck_weights) -> int:
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
