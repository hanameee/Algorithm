from collections import defaultdict


def solution(nums):
    answer = []
    n = len(nums)
    chk = defaultdict(list)
    nums = sorted((nums))
    for i in range(0, len(nums)-2):
        target = -(nums[i])
        l = i+1
        r = len(nums)-1
        while l < r:
            if nums[l]+nums[r] == target:
                if nums[l] in chk[nums[i]]:
                    l += 1
                    continue
                answer.append([nums[i], nums[l], nums[r]])
                chk[nums[i]].append(nums[l])
                l += 1
            if nums[l]+nums[r] < target:
                l += 1
            else:
                r -= 1
    return answer


# print(solution([-1, 0, 1, 2, -1, -4]))
# print(solution([0, 0, 0, 0]))
# print(solution([-2, 0, 0, 2, 2]))
# print(solution([3, 0, -2, -1, 1, 2]))
print(solution([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
