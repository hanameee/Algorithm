# [210] Course Schedule II

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | Easy **Medium** Hard             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 30분                          |
| 시간복잡도  |                                  |

## Result

![210](210.png)

## Solving

207번이랑 완전 동일한 문제라 코드 복붙... 'v'

근데 Leetcode의 시간복잡도/공간복잡도 계산 시스템 너무 이상하다. 첫번째 제출했을땐 96ms였는데 똑같은거 다시 제출하니까 72ms 🤷🏻‍♀️

## Source

```python
from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        v, e = numCourses, len(prerequisites)
        indegree = [0] * (v)
        graph = [[] for i in range(v)]
        result = []
        q = deque()
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        for i in range(v):
            if indegree[i] == 0:
                q.append(i)
        while q:
            curr_node = q.popleft()
            result.append(curr_node)
            for i in graph[curr_node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if len(result) == numCourses:
            return result
        else:
            return []
```