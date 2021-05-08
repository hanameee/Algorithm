# [111] Minimum Depth of Binary Tree

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | **Easy** Medium Hard             |
| 체감 난이도 | **Easy** Medium Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 30분                          |
| 시간복잡도  | O(V+E)                           |

## Result

![111](111.png)

## Solving

Deque를 이용한 BFS로 풀었고, 처음에는 최대 깊이로 생각하고 풀었다가 예시 테케를 통과 못해서 문제를 다시 읽었습니다.

또, 빈 input  `[]` 이 들어왔을 경우를 놓쳐서 한번 틀린 뒤 예외처리 했습니다.

## Source

```python
from collections import deque

class Solution(object):        
    def minDepth(self, root):
        if root:
            depth = 1
            q = deque([[root, depth]])
            while q:
                curr, d = q.popleft()
                if not curr.left and not curr.right:
                    return d
                if curr.left:
                    q.append([curr.left, d+1])
                if curr.right:
                    q.append([curr.right, d+1])
                depth = max(depth, d)
            return depth
        else:
            return 0
```

