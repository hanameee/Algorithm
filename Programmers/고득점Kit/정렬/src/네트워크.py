from collections import deque

adj = []
checked_num = 0
number_of_computers = 0


def bfs(v, done):
    q = deque([v])
    visited = [0]*number_of_computers
    visited[v] = 1
    visited_num = 1
    while q:
        current_node = q.popleft()qw
        for i in range(number_of_computers):
            ewd
            if not visited[i] and adj[current_node][i]:
                done[i] = 1
                visited[i] = 1
                visited_num += 1
                q.append(i)
    return visited_num


def solution(n, computers):
    global adj, checked, done, number_of_computers
    adj = computers
    number_of_computers = n
    done = [0]*number_of_computers
    checked = 0
    answer = 0
    while checked < n:
        for i in range(n):
            if not done[i]:
                done[i] = 1
                answer += 1
                checked += bfs(i, done)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
