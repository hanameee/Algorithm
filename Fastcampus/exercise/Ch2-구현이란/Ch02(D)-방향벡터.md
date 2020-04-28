# Ch 02(D) - 방향벡터

우리는 코딩테스트를 풀면서 **방향**에 관련된 문제를 많이 풀게 된다.

대표적인 문제가 BFS/DFS를 활용하는 2,3차원 배열의 이동이 있다. 그래프보단 2차원, 3차원 배열이 많다.

탐색/확인 방향의 예시는

- 상하좌우
- 상하좌우+대각선
- 나이트, 말

### 상하좌우

조건문을 활용할 수도 있지만, 아래처럼 활용하면 조건문 없이 편하게 사용할 수 있다

```python
# 얘는 상하좌우
dx = [-1,1,0,0]
dy = [0,0,1,-1]
# 얘는 반시계 방향 (상, 좌, 하, 우)
dx = [0,-1,0,1]
dy = [1,0,-1,0]
# 얘는 시계 방향 (상, 우, 하, 좌)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
```

예를 들어 다음과 같이 풀 수 있다.

```python
# 동서남북이 문자열로 주어지면 index를 활용해서!
x += dx['ENSW'.index(way)]
y += dy['ENSW'.index(way)]
```

일반적으로 dfs에서는 다음과 같이 활용한다.

```python
for i in range(4):
  dfs(x+dx[i], y+dy[i])
```

---

## 16956. 늑대와 양

그냥... 울타리에... 다... 두면 된다...



## 14620. 꽃길 ⭐️

전수조사 + 방향벡터

**그리디하게 작은 것부터 채우는게 최소가 아닐 수 있다**. n의 수가 적으므로 조합을 다 구해서 완전탐색을 진행해야 한다!

n의 수가 적으면, 항상 완전탐색은 아닌가? 생각해야 한다.

```python
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
mp = [list(map(int, input().split())) for i in range(n)]
# 자기 자신도 고려해야 하므로 (이동하지 않는) 0,0도 추가해주기!
dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
price = [[0]*n for i in range(n)]
sorted_price = []
result = 10000


def is_available_combination(combination):
    visited = [[0]*n for i in range(n)]
    for data in combination:
        price, x, y = data
        for d in range(5):
            nx = x+dx[d]
            ny = y+dy[d]
            if visited[nx][ny] != -1:
                visited[nx][ny] = -1
            else:
                return False
    return True


for i in range(1, n-1):
    for j in range(1, n-1):
        p = 0
        for d in range(5):
            nx = i+dx[d]
            ny = j+dy[d]
            p += mp[nx][ny]
        price[i][j] = p
        sorted_price.append((price[i][j], i, j))
sorted_price.sort()

for combination in combinations(sorted_price, 3):
    if is_available_combination(combination):
        a, b, c = combination
        result = min(result, a[0]+b[0]+c[0])

print(result)
```

100만, 1000만 정도의 시간이 든다면 완전탐색인거다!