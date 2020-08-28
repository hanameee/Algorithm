def solution(nums):
    nums = sorted(nums)
    filtered_nums = [v for (idx, v) in enumerate(nums) if idx % 2 == 0]
    print(filtered_nums)
    return sum(filtered_nums)


print(solution([1, 4, 3, 2]))
