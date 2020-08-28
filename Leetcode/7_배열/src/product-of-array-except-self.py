def solution(nums):
    n = len(nums)
    l_product = nums[::]
    for i in range(1, n):
        l_product[i] *= l_product[i-1]
    r_product = nums[::]
    for i in range(n-2, 0, -1):
        r_product[i] *= r_product[i+1]
    answer = [0]*len(nums)
    answer[0] = r_product[1]
    answer[-1] = l_product[-2]
    for i in range(1, len(nums)-1):
        answer[i] = l_product[i-1]*r_product[i+1]
    return answer


print(solution([1, 1]))
