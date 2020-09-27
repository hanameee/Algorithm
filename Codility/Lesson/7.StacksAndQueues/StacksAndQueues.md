# [Brackets](https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/)

```python
def solution(S):
    if len(S) == 0:
        return 1
    matching_map = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    stk = []
    for s in S:
        if s in ["(","{","["]:
            stk.append(s)
        else:
            if not stk:
                return 0
            elif stk[-1] == matching_map[s]:
                stk.pop()
    if len(stk) != 0:
        return 0
    else:
        return 1
```

시험때는 코드 제출 여러번 못한다. 예외처리 똑디 하자!



# [Fish](https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/)

```python
def solution(A, B):
    stk = []
    for idx in range(len(B)-1,-1,-1):
        if B[idx] == 0:
            stk.append((0,A[idx]))
        else:
            eaten = False
            while stk and stk[-1][0] == 0:
                if stk[-1][1] < A[idx]:
                    stk.pop()
                else:
                    eaten = True
                    break
            if not eaten or stk[-1][0] == 1:
                stk.append((1,A[idx]))
    return len(stk)
```

문학적인(?) 스택 문제 🐟

괄호와는 달리, 한 물고기가 여러 방향이 다른 물고기를 먹을 수 있기 때문에 자기가 먹히거나/ 끝까지 다 먹을 때까지 계속해서 스택을 타고 내려가도록 while로 처리를 해줘야 한다.



# [Nesting](https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/)

기본중의 핵기본 스택문제. 빈 문자열 처리하는 것 외엔 예외처리 할 것도 없다.

```python
def solution(S):
    if len(S) == 0:
        return 1
    stk = []
    for s in S:
        if s == "(":
            stk.append(s)
        else:
            if not stk:
                return 0
            else:
                if stk[-1] == "(":
                    stk.pop()
    if stk:
        return 0
    else:
        return 1
```



# [StoneWall](https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/)

```python
def solution(H):
    stk = []
    answer = 0
    for h in H:
        while True:
            if not stk:
                answer += 1
                stk.append(h)
                break
            else:
                if stk[-1] == h:
                    break
                elif stk[-1] <= h:
                    stk.append(h)
                    answer += 1
                    break
                elif stk[-1] > h:
                    stk.pop()
    return answer
```

얘도 뭔가 좀 이해하기가 힘들었다. 스택 문제인걸 모르고 풀었으면 한참 걸렸을 것 같음.

기본적으로 **같은 높이의 블록이 연이어서 나오면 재사용이 가능**하다. 같은 높이의 블록 사이에 더 높은 블록이 있는 것은 문제가 되지 않지만, 더 낮은 블록이 있다면 재사용 할 수 없다.

이건 예제를 보면서 스택에 넣어보면 조금 더 이해가 쉽다.

스택에 앞에서부터 하나씩 넣으면서

1) top이 지금 블록과 같다면 pop 후 break (재사용했으므로 블록 갯수 증가 X)

2) top이 지금 블록보다 크다면 작거나/같은것이 나올때까지 pop

3) top이 지금 블록보다 작다면 사용한 블록 갯수에 +1을 하고 append후 break

4) stk이 비었다면 append하고 사용한 블록 갯수에 +1

내가 풀었는데도 이해가 잘 안됨. 다시 풀어봐야지...

