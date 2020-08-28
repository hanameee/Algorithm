def solution(height):
    if not height:
        return 0
    answer = 0
    l, r = 0, len(height)-1
    l_max, r_max = height[l], height[r]
    while l < r:
        l_max, r_max = max(height[l], l_max), max(height[r], r_max)
        if l_max <= r_max:
            answer += l_max - height[l]
            l += 1
        else:
            answer += r_max - height[r]
            r -= 1
    return answer


print(solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
