def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0
    while left <= right:
        prev = 0
        min_gap = distance
        removed_rocks = 0
        mid = (left+right)//2
        for rock in rocks:
            if rock - prev < mid:
                removed_rocks += 1
            else:
                # 징검다리 간격의 최소값을 기록한다
                min_gap = min(min_gap, rock-prev)
                prev = rock
        # 제한을 낮춰 삭제하는 돌의 갯수를 줄여야 한다
        if removed_rocks > n:
            right = mid-1
        # 제한을 높여 삭제하는 돌의 갯수를 늘려야 한다
        else:
            answer = min_gap
            left = mid + 1
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
