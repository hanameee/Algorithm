from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque([[i, 0] for i in truck_weights])
    total_weight = 0
    time = 0
    while truck_weights:
        time += 1
        if truck_weights[0][1] == bridge_length:
            total_weight -= truck_weights[0][0]
            truck_weights.popleft()
        for truck in truck_weights:
            if truck[1] != 0:
                truck[1] += 1
            else:
                if total_weight + truck[0] <= weight:
                    total_weight += truck[0]
                    truck[1] += 1
                break
    return time


print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
