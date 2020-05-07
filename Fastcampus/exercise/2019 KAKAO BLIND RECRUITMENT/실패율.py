# 12:11~
def solution(n, stages):
    users = [0]*(n+1)
    not_users = [0]*(n+1)
    failure_ratio = [(0, idx) for idx in range(1, n+1)]
    for s in stages:
        # 특정 단계에 머무르고 있는 사람이라면
        if s != n+1:
            for i in range(1, s+1):
                users[i] += 1
            not_users[s] += 1
        else:
            for i in range(1, s):
                users[i] += 1
    for i in range(1, n+1):
        if users[i] == 0:
            failure_ratio[i-1] = [0, i]
        else:
            failure_ratio[i-1] = (not_users[i]/users[i], i)
    failure_ratio.sort(key=lambda x: (-x[0], x[1]))
    answer = []
    for _, idx in failure_ratio:
        answer.append(idx)
    return answer


print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))
