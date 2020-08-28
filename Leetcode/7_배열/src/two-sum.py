from collections import defaultdict


def twoSum(nums, target):
    max_len = max(nums)
    dic = defaultdict(list)
    for idx in range(len(nums)):
        dic[nums[idx]].append(idx)
    for idx in range(len(nums)):
        if len(dic[(target-nums[idx]]):
            for candidate in dic[target-nums[idx]]:
                if candidate != idx:
                    return [idx, candidate]


print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([-1, -2, -3, -4, -5], -8))
