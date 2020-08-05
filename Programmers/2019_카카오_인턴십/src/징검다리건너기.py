from copy import deepcopy


def get_gap(stones, mid, k):
    gap = 0
    for stone in stones:
        if stone < mid:
            gap += 1
        else:
            if gap:
                if gap >= k:
                    return False
                gap = 0
    if gap:
        if gap >= k:
            return False
    return True


def solution(stones, k):
    sorted_stone = sorted(stones)
    mx = sorted_stone[-1]
    mn = sorted_stone[0]
    answer = mn
    # 이분탐색
    while mn <= mx:
        mid = (mx+mn)//2
        result = get_gap(stones, mid, k)
        if result:
            answer = max(mid, answer)
            mn = mid + 1
            continue
        else:
            mx = mid - 1
            continue
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
