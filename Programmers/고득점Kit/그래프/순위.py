from collections import Counter


def dfs(target, idx, result):
    if result > 0:
        for i, r in enumerate(result_matrix[idx]):
            if not result_matrix[target][i]:
                if r > 0:
                    result_matrix[target][i] = 1
                    dfs(target, i, r)
    else:
        for i, r in enumerate(result_matrix[idx]):
            if not result_matrix[target][i]:
                if r < 0:
                    result_matrix[target][i] = -1
                    dfs(target, i, r)
    return


def solution(n, results):
    global result_matrix
    result_matrix = [[0]*(n+1) for _ in range(n+1)]
    for win, lose in results:
        result_matrix[win][lose] = 1
        result_matrix[lose][win] = -1
    for i in range(1, n+1):
        for idx, result in enumerate(result_matrix[i]):
            if result:
                dfs(i, idx, result)
    answer = 0
    for num in range(1, n+1):
        count = Counter(result_matrix[num])
        if count[0] == 2:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(5, [[5, 4], [4, 3], [3, 2], [2, 1]]))
