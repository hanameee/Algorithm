def solution(n, lost, reserve):
    clothes = [1 for i in range(n)]
    for l in lost:
        clothes[l-1] = 0
    for r in reserve:
        clothes[r-1] += 1
    answer = n
    for idx in range(n):
        if clothes[idx] == 0:
            if idx >= 1 and idx <= n-2:
                if clothes[idx-1] == 2:
                    clothes[idx-1] -= 1
                    continue
                if clothes[idx+1] == 2:
                    clothes[idx+1] -= 1
                    continue
            elif idx < 1:
                if clothes[idx+1] == 2:
                    clothes[idx+1] -= 1
                    continue
            else:
                if clothes[idx-1] == 2:
                    clothes[idx-1] -= 1
                    continue
            answer -= 1
    return answer
