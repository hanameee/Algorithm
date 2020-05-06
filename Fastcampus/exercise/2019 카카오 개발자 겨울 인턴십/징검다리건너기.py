from copy import deepcopy


# 인덱스 i의 stones는 몇번째 최소값인가를 dp에 저장
def solution(stones, k):
    sorted_stones = []
    nth_small = [0]*len(stones)
    for idx, stone in enumerate(stones):
        sorted_stones.append((stone, idx))
    sorted_stones.sort()
    prev_value = 0
    idx_count = 0
    min_value_lst = [0]*len(stones)
    for nth_idx in range(len(sorted_stones)):
        stone_value, stone_idx = sorted_stones[nth_idx]
        if stone_value == prev_value:
            nth_small[stone_idx] = nth_small[sorted_stones[nth_idx-1][1]]
        else:
            nth_small[stone_idx] = idx_count
            min_value_lst[idx_count] = stone_value
            idx_count += 1
        prev_value = stone_value
    # nth_small 중 k개의 연속합의 최소값을 구하면 됨
    n = len(stones)
    if n == 1:
        return(stones[0])
    if n == k:
        return(max(min_value_lst))
    acc_sum = [0]*(n-k+1)
    answer = 1e9
    for i in range(0, n-k):
        maximin = 0
        for j in range(k):
            maximin = max(maximin, min_value_lst[nth_small[i+j]])
        answer = min(maximin, answer)
    return answer


print(solution([1, 2, 1], 3))
# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
