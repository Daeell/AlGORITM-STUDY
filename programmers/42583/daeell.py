from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    time = 0
    truck_weights = deque(truck_weights)
    bridge_weight = 0

    while truck_weights:
        time += 1
        bridge_weight -= bridge.popleft()
        if bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)

    time += bridge_length

    return time


print(solution(2, 10, [7, 4, 5, 6]))
