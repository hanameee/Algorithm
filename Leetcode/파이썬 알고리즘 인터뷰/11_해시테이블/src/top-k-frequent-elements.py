# from collections import Counter


# def solution(nums, k):
#     freq = Counter(nums)
#     result = [value for value, count in freq.most_common(k)]
#     return result


# print(solution([1, 1, 1, 2, 2, 3], 2))

info = {1: "a", 2: "b", 3: "c"}
new_info = {**info, 3: "d"}
print(new_info)
