import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    total_length = 0
    for operation in operations:
        oper_arr = operation.split(" ")
        value = int(oper_arr[1])
        if oper_arr[0] == "I":
            heapq.heappush(max_heap, -value)
            heapq.heappush(min_heap, value)
            total_length += 1
        else:
            if total_length < 1:
                continue
            if value == 1:
                heapq.heappop(max_heap)
                total_length -= 1
            else:
                heapq.heappop(min_heap)
                total_length -= 1
            if total_length == 0:
                max_heap = []
                min_heap = []
        print(operation, max_heap, min_heap)
    if total_length == 0:
        return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]


# print(solution(["I -3", "I 0", "I -2", "I -1", "D 1", ]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1",
                "D 1", "D -1", "D -1", "I 5", "I 6"]))
# print(solution(["I 7", "I 5", "I -5", "D -1"]	))
