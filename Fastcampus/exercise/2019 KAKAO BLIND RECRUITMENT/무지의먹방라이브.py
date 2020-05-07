def solution(food_times, k):
    times = {}
    for idx, time in enumerate(food_times):
        if time in times:
            times[time].append(idx)
        else:
            times[time] = [idx]
    len_foods = len(food_times)
    cycle = 0
    print(times)
    for time in sorted(times):
        # 아직 싸이클 덜 돌았을때
        if k - (len_foods*(time-cycle)) >= 0:
            k -= len_foods*(time-cycle)
            len_foods -= len(times[time])  # 최소값이 여러개라면 갯수만큼 빼준다
            cycle += time-cycle
        # 싸이클 다 돌았을때, 현재 time은 직전에 다 먹은 음식
        else:
            k %= len_foods  # k가 해당 원판에서 몇번째 음식을 먹어야하는지
            for i in times:
                print(times, i, time)
                # 이 times는 sort되지 않음. 즉, 먼저 걸리는 애가 더 먼저 위치했던 애.
                if i >= time:
                    # 저번에 먹은 음식보다 크거나 같으면서 제일 먼저 나오는 애의 index
                    idx = times[i][0]
                    break
            for i in range(idx, len(food_times)):
                if food_times[i] >= time:
                    if k == 0:
                        return i+1
                    k -= 1
    return -1


# print(solution([3, 1, 2], 5))
print(solution([2, 1, 1, 1, 2, 5, 3], 1))
