# [116] Populating Next Right Pointers in Each Node

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | Easy **Medium** Hard             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 30분                         |
| 시간복잡도  | O(V+E)                           |

## Result

![116](116.png)

## Solving

next가 가르키는 순서가 BFS 형태라 deque를 사용한 BFS로 풀었다.

## Source

```python
from collections import deque

class Solution(object):
    def connect(self, root):
        queue = deque([root])
        level = 0
        idx = 0
        while queue:
            r = queue.popleft()
            if r:
                idx += 1
                if idx == 2**level:
                    r.next = None
                    level += 1
                    idx = 0
                else:
                    r.next = queue[0]
                if r.left:
                    queue.append(r.left)
                    queue.append(r.right)
        return root
```

