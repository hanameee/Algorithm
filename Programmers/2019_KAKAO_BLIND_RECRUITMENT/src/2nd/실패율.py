def solution(n, stages):
    person_tried = [0] * (n + 1)
    person_failed = [0] * (n + 1)
    answer = []
    for s in stages:
        if s == n + 1:
            for i in range(1, s):
                person_tried[i] += 1
            continue
        for i in range(1, s + 1):
            person_tried[i] += 1
        person_failed[s] += 1
    fail = [[0, i] for i in range(0, n + 1)]
    for i in range(1, n + 1):
        if person_tried[i]:
            fail[i][0] = person_failed[i] / person_tried[i]
        else:
            fail[i][0] = 0
    fail = sorted(fail[1:], key=lambda x: -x[0])
    for f in fail:
        answer.append(f[1])
    return answer


print(solution(4, [4, 4, 4, 4, 4]))
