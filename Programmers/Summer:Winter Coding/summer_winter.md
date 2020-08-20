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

