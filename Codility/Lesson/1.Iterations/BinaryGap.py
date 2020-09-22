def solution(n):
    binary_arr = []
    while n != 0:
        binary_arr.append(n % 2)
        n = n//2
    max_gap = 0
    cumm_sum = 0
    gap = 0
    for item in binary_arr:
        if cumm_sum == 1 and not item:
            gap += 1
        else:
            cumm_sum += item
        if cumm_sum == 2:
            cumm_sum = 1
            max_gap = max(gap, max_gap)
            gap = 0
    return max_gap
