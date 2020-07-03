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