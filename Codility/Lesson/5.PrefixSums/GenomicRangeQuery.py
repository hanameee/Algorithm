def get_idx(s):
    if s == "A":
        return 1
    if s == "C":
        return 2
    if s == "G":
        return 3
    if s == "T":
        return 4


def solution(S, P, Q):
    answer = [0 for i in range(len(P))]
    arr = [[-1 for _ in range(5)] for i in range(len(S))]
    arr[0][get_idx(S[0])] = 0
    for i in range(1, len(S)):
        arr[i] = arr[i-1][:]
        arr[i][get_idx(S[i])] = i
    for j in range(len(P)):
        for k in range(1, 5):
            if arr[Q[j]][k] >= P[j]:
                answer[j] = k
                break
    print(arr)
    return answer


print(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]))
