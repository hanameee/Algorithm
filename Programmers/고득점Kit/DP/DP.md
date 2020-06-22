## 등굣길

문제에서의 최단거리의 정의로 인해 하,우 이동만 생각하면 돼서 평이한 문제였지만 실수할 만한 부분이 많았다.

일단 문제에서 m,n을 기존 좌표 문제의 x,y와는 조금 다르게 주기 때문에 좌표부터 헷갈렸고, puddle만 생각하는 것이 아니라 puddle로 인해 연속적으로 못가게 되는 곳을 잘 생각해야 한다.

```python
def solution(m, n, puddles):
    if m == 1 or n == 1:
        return 1
    mp = [[0]*m for i in range(n)]
    for x, y in puddles:
        mp[y-1][x-1] = -1
    for i in range(m):
        if mp[0][i] == -1:
            mp[0][i] = 0
            for j in range(i+1, m):
                mp[0][j] = 0
            break
        else:
            mp[0][i] = 1
    for i in range(n):
        if mp[i][0] == -1:
            mp[i][0] = 0
            for j in range(i+1, n):
                mp[j][0] = 0
            break
        else:
            mp[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            if mp[i][j] == -1:
                mp[i][j] = 0
                continue
            mp[i][j] = (mp[i-1][j] + mp[i][j-1]) % 1000000007
    answer = (mp[n-1][m-1]) % 1000000007
    return answer


print(solution(4, 3, [[3, 1], [2, 2]]))
```

1. 초기화 할 때 모든 구간을 1로 초기화 하고, puddle만 0으로 초기화 하면 안된다.

   puddle에 의해 아예 못 가게 되는 곳이 있을 수 있다. 예를 들어, [1,2]와 [2,1]이 모두 puddle이라면, [2,2]는 puddle에는 없지만 사실상 못 가는 곳이기 때문이다.

2. puddle로 인해 못가는 구간을 잘 파악해야 한다.

   puddle이 0열 혹은 0행에 있을 시 못 가는 부분을 간다고 착각할 수 있다. [0,1]이 puddle이면 [0,2]~[0,n]은 전부 다 못간다.

아무튼 코드를 좀 지저분하게 짠 것 같다. 시무룩.

[모범 답안]

내가 index error 방지하려고 1,1부터 돌아서 복잡도가 증가했던 것 같다.

애초에 **행/열을 하나씩 더** 만들었다면 index error도 걱정할 필요 없고, 0열 혹은 0행에도 똑같은 점화식(`[a,b] = [a-1,b] + [a,b-1]`)을 적용해서 별도의 코드 없이도 못가는 부분을 체크할 수 있다.

```python
def solution(m, n, puddles):
    mp = [[0]*(m+1) for i in range(n+1)]
    for x, y in puddles:
        mp[y][x] = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                mp[i][j] = 1
                continue
            if mp[i][j] == -1:
                mp[i][j] = 0
                continue
            mp[i][j] = (mp[i-1][j] + mp[i][j-1]) % 1000000007
    answer = (mp[n][m]) % 1000000007
    return answer
```

이렇게 하면 깔끔! :)

이런 좌표 문제를 풀 때는, 행/열을 하나씩 더 만드는 습관을 들이는 것이 좋을 것 같다. 불필요한 복잡도를 낮춰준다.