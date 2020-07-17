def solution(n, path, order):
    # ���� �׷��� ������ֱ�
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
    # �ڽ� ��� �����ϱ�
    print(adj)
    return True


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [
    1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
