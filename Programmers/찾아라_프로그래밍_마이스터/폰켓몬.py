def solution(nums):
    nums_set = set(nums)
    if len(nums_set) >= nums//2:
        return nums//2
    else:
        return len(nums_set)


print(solution([3, 3, 3, 2, 2, 2]))
