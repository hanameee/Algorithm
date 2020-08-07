from copy import deepcopy


def is_solved(graph, m, n):
    for i in range(m-1, m-1+n):
        for j in range(m-1, m-1+n):
            if graph[i][j] != 1:
                return False
    return True


def rotate(key):
    new_key = [[0]*len(key[0]) for _ in range(len(key[0]))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key)-i-1] = key[i][j]
    return new_key


def process(key, graph, m, n):
    g_len = len(graph)
    for i in range(m-1+n):
        for j in range(m-1+n):
            g = deepcopy(graph)
            # 키를 적용시켜본다
            for key_i in range(len(key)):
                if i+key_i > n+m-1:
                    break
                for key_j in range(len(key)):
                    g[i+key_i][j+key_j] += key[key_i][key_j]
            if is_solved(g, m, n):
                return True
    return False


def solution(key, lock):
    m = len(key)
    n = len(lock)
    mp = [[0]*(n+2*(m-1)) for _ in range(n+2*(m-1))]
    for i in range(m-1, m-1+n):
        for j in range(m-1, m-1+n):
            mp[i][j] = lock[i-m+1][j-m+1]
    rotated_keys = [key]
    for i in range(3):
        new_key = rotate(key)
        rotated_keys.append((new_key))
        key = new_key
    for key in rotated_keys:
        result = process(key, mp, m, n)
        if result:
            return True
    return False


print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
