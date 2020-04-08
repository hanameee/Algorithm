## 타겟 넘버

한번에 맞은게 얼마만이야 깔깔 (디버깅은 제외한다 😏)
BFS로 풀었다. DFS는 뭔가 스택 터질까봐 무섭단 말이지...

2^20 이어도 1,000,000 정도 되는 숫자이기에 완전탐색해도 무방하다. (1초에 2천~5천만번까지 OK)
DFS로도 다시 한번 풀어볼 것.

```python
from collections import deque

data = []


def bfs(v, target):
    q = deque([v])
    depth = 0
    number = data[0]
    while q:
        for i in range(len(q)):
            current_node = q.popleft()
            for adj_node in [current_node-number, current_node+number]:
                q.append(adj_node)
        depth += 1
        if depth == len(data):
            break
        else:
            number = data[depth]
    target_number = 0
    for num in q:
        if num == target:
            target_number += 1
    return target_number


def solution(numbers, target):
    global data
    data = numbers
    answer = bfs(0, target)
    return answer
```

---

## 네트워크

기본적인 탐색 구현 문제였던 것 같다.

```python
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
        current_node = q.popleft()
        for i in range(number_of_computers):
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
```

---

