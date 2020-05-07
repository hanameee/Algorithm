# 1:09~


def solution(n, weak, dist):
    # (갯수,이동거리,시작,끝)
    lst = []
    checked_position = []
    max_dist = max(dist)
    for i in range(len(weak)-1):
        for j in range(i, len(weak)):
            # if i == j or (j, i) in checked_position:
            #     continue
            # 시계방향 체크
            if not (weak[j]-weak[i] > max_dist or weak[j]-weak[i] < 0):
                points = []
                for point in weak:
                    if point <= weak[j] and point >= weak[i]:
                        points.append(point)
                lst.append((
                    len(points), weak[j]-weak[i], weak[i], weak[j], points))
                checked_position.append((i, j))
            # 반시계방향 체크
            if not (n-abs(weak[i]-weak[j]) > max_dist):
                points = []
                for point in weak:
                    if point >= weak[j] or point <= weak[i]:
                        points.append(point)
                lst.append((
                    len(points), n-abs(weak[i]-weak[j]), weak[i], weak[j], points))
                checked_position.append((i, j))
    # 많이 갈 수 있는 친구부터, 갯수가 많은 것부터 시도해본다.
    # lst = (갯수,이동거리,시작,끝)
    lst.sort(key=lambda x: -x[1])
    for _ in lst:
        print(_)
    min_count = 1e9
    # 처음 선택하는 것 이동하기
    for i in range(len(lst)-1):
        used_friend = [False]*len(dist)
        count = 0
        done = set([])
        breaker = False
        # 케이스들
        for lst_idx in range(i, len(lst)):
            # 한 점이라도 이미 done에 있다면 최적이 아니므로 이후 코드 실행하지 않고 바로 다음 코드
            for weak_point in lst[lst_idx][-1]:
                if weak_point in done:
                    breaker = True
                    break
            if breaker:
                continue
            start_done_idx = len(done)
            for f_idx in range(len(dist)-1, -1, -1):
                if start_done_idx != len(done):
                    break
                # 아직 안 쓴 친구들에 대해
                if used_friend[f_idx] == False:
                    # 친구가 갈 수 있는 곳이라면
                    if lst[lst_idx][1] <= dist[f_idx]:
                        count += 1
                        used_friend[f_idx] = True
                        for weak_point in lst[lst_idx][-1]:
                            done.add(weak_point)
                        if len(done) == len(weak):  # 다 갔다면
                            min_count = min(count, min_count)
                            break
            if len(done) == len(weak):
                break
    return min_count
# 지점이 아닌 곳에서 시작할 필요 없음
# 지점을 출발점으로 삼으면 됨
# 시계방향 또는 반시계방향으로 돌 수 있음
# 출발점, 도착점, 방향, 그 안의 weak 개수 를 체크하면 될 것 같음


print(solution(30, [0, 3, 11, 21], [10, 4]))
# print(solution(12, 	[1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(50, [1, 5, 10, 12, 22, 25], [4, 3, 2, 1]))
# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
