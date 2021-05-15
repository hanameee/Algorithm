# [112] Path Sum

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

![112](112.png)

## Solving

문제 자체는 108번보다 쉬운데, 클래스 변수 사용법이 헷갈려서 한번 헤매고 + 빈 root가 들어왔을때 처리 안해서 두번 헤맸습니다.

total 값을 더해가면서 재귀적으로 dfs를 돌리고, left node에서 total 값이 targetSum과 일치하는지, 일치한다면 return 해주는 방식으로 풀었습니다.

## Source

```python
class Solution(object):
    flag = False
    def hasPathSum(self, root, targetSum):
        def dfs(curr, total):
            if self.flag:
                return
            total += curr.val
            if curr.left != None:
                dfs(curr.left, total)
            if curr.right != None:
                dfs(curr.right, total)
            if curr.left == None and curr.right == None:
                if total == targetSum:
                    self.flag = True
        if root:
            total = root.val
            if root.left != None:
                dfs(root.left, total)
            if root.right != None:
                dfs(root.right, total)
            if root.left == None and root.right == None:
                if total == targetSum:
                    self.flag = True
        return self.flag
```

