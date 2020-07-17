def solution(n, path, order):
    # 인접 그래프 만들어주기
    adj = [0]*n
    for a, b in path:
        if adj[a]:
            adj[a].append(b)
        else:
            adj[a] = [b]
        if adj[b]:
            adj[b].append(a)
        else:
            adj[b] = [a]
    # 자식 노드 저장하기
    print(adj)
    return True


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [
    1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
