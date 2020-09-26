# [Summer/Winter Coding](https://programmers.co.kr/learn/courses/30/lessons/49993)

## 멀쩡한 사각형

어떠한 패턴이 반복된다는 것은 알았는데, 그걸 정확하게 풀어내기가 어려운 문제였다.

a,b가 서로소라면 (겹치는 약수가 없다면) 대각선으로 갈라지는 사각형의 갯수는 a+b-1개이고, a,b에 공약수가 존재한다면 a,b를 최대공약수로 나눈 값으로 a'+b'-1을 구하고, 거기에 최대공약수만큼을 곱해주면 된다.

```python
import math


def get_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a = a % b
        a, b = b, a
    return a


def solution(w, h):
    total_rects = w*h
    gcd = get_gcd(w, h)
    if gcd == 1:
        return total_rects - w+h-1
    else:
        return total_rects - ((w//gcd)+(h//gcd)-1)*gcd


print(solution(8, 12))
```



## 124 나라의 숫자

n진법의 원리를 사용하면 풀 수 있는 문제. 숫자가 1,2,4밖에 없으므로 3진법과 원리는 완전히 동일하지만, 3,6 등 3으로 올라갈 때 예외를 두어야 한다. 다음 자릿수로 올라가는게 아니라 (10이 아니라 4가 되어야 함) 4가 되기 때문에!

계속해서 3으로 나눠서 나머지를 기록하는 식으로 하고, 

```python

```



## 스킬트리

```python
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_arr = []
        for t in tree:
            if t in skill:
                skill_arr.append(t)
        new_skill = "".join(skill_arr)
        if new_skill == skill[:len(new_skill)]:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
```

무조건 선행 스킬을 배워야 하므로, 선행 스킬에 포함되지 않은 글자를 제외한 문자열은 무조건 스킬 트리의 맨 앞에서부터 length만큼 slice한 문자열과 일치해야 한다.



## 방문 길이

문제를 가만히 읽어보니, 카카오 2020 인턴십에서 나온 `경주로 건설`과 유사한 문제라는것이 보였다. 반가웠다...🥺

**지나간 길**은, 기존의 길찾기 문제에서 많이 본 **방문한 지점**과는 다르다.

처음에는 A->B 에서 A지점도 방문, B지점도 방문이면 지나간 길이라고 생각했는데 아니다. A->B, C->D 를 지나갔을때 B,D 두 지점을 모두 방문했을지라도 B->D는 지나간 길이 아니기 때문이다.

결과적으로 한 지점당 4개의 정보를 저장해야 한다. 상하좌우 길 중 지나간 길의 정보를 담는 것이다.

A->B 일때, A에서 U 방향으로 이동했다면 A지점에서는 U가 true, B지점에서는 D가 true가 된다. 이렇게 지점마다 4방향 길의 지나감 정보를 저장해두고, dirs를 돌면서 현재 지점/방문예정 지점에서 해당 방향의 길의 boolean 값을 체크한다.

```python
def solution(dirs):
    directions = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    opposite_dir = {"U": "D", "D": "U", "R": "L", "L": "R"}
    mp_dict = {"U": [[0]*11 for _ in range(11)],
               "D": [[0]*11 for _ in range(11)],
               "R": [[0]*11 for _ in range(11)],
               "L": [[0]*11 for _ in range(11)]}
    curr_location = [5, 5]
    answer = 0
    for dir in dirs:
        [x, y] = curr_location
        dx, dy = directions[dir]
        nx, ny = dx+x, dy+y
        if nx < 0 or ny < 0 or nx > 10 or ny > 10:
            continue
        curr_location = [nx, ny]
        if mp_dict[dir][x][y] or mp_dict[opposite_dir[dir]][nx][ny]:
            continue
        mp_dict[dir][x][y] = 1
        mp_dict[opposite_dir[dir]][nx][ny] = 1
        answer += 1
    return answer
```

## 숫자 게임

A,B 둘다 정렬을 하고 풀면 되는 간단한 문제다. 

쉽게 생각하면, 제일 작은 B부터 시작해서 A를 이길 때까지? B의 인덱스를 증가시키면 된다.

```js
def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    b = 0
    for a in A:
        if a >= B[b]:
            while a >= B[b]:
                b += 1
                if b == len(B):
                    return answer
        answer += 1
        b += 1
        if b == len(B):
            return answer
    return answer
```

## 기지국 설치

대충 풀면 틀린다. 수도코드 똑바로 쓰고 난 다음에 코드 쓰기!

```python
import math


def solution(n, stations, w):
    start_idx = 0
    answer = 0
    gap = w*2+1
    for station in stations:
        if start_idx >= n:
            break
        end_idx = station-1-w-1
        if start_idx > end_idx:
            start_idx = station+w
            continue
        else:
            answer += math.ceil((end_idx-start_idx+1)/gap)
            start_idx = station+w
    if start_idx < n:
        answer += math.ceil((n-start_idx)/gap)
    return answer
```

기본적으로 input의 크기가 2억이기때문에 하나씩 탐색하면 효율성 터진다.

힌트는 stations의 크기가 **10000 이하의 자연수**라는 데에 있다. 10000은 만만따리한 숫자이기 때문에 loop을 돌아도 되기 때문이다. 따라서 stations를 하나씩 돌면서, 이 전 station이 커버하지 못한 곳 ~ 지금 station이 커버하지 못한 곳을 파악한다.

이 전 station이 5까지 커버하고, 지금 station이 15부터 커버했다면 6~14는 빈 공간이 된다. w가 2라면 하나의 w를 놓을 때마다 5칸을 커버할 수 있다. 따라서 6~14를 커버하기 위해서는 9칸을 채워야 하고, 그러려면 math.ceil(9/5) 만큼의 station을 추가로 증설해야 한다.

idx가 1부터 주어지는 것이 조금 헷갈리고, stations가 겹칠 수도 있고, (5~10을 커버하는 station 뒤에 바로 6~11을 커버하는 station이 올 수도 있다.) station이 커버하는 idx가 n을 넘어버릴 수도 있기 때문에 (n=15인데 14에 양쪽으로 2씩 커버하는 station을 놓는다던가) 이런 부분을 조금 조심해서 처리해줘야 한다.

## 배달

```python
import heapq


def solution(N, road, K):
    adj = [[] for i in range(N+1)]
    dist = [float("inf") for i in range(N+1)]
    dist[1] = 0
    need_visit = [(0, 1)]
    for r in road:
        a, b, c = r
        adj[a].append((c, b))
        adj[b].append((c, a))
    while need_visit:
        curr_dist, curr_v = heapq.heappop(need_visit)
        for adj_dist, adj_v in adj[curr_v]:
            if dist[adj_v] > adj_dist+curr_dist:
                dist[adj_v] = adj_dist+curr_dist
                heapq.heappush(need_visit, (dist[adj_v], adj_v))
    answer = 0
    for d in dist:
        if d <= K:
            answer += 1
    return answer

```

기본적인 다익스트라 최단 경로 문제. 다익스트라는 사실상 최단경로 배열만 추가적으로 관리하는 BFS라고 볼 수 있다.

