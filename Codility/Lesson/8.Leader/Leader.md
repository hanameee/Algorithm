# [Dominator](https://app.codility.com/programmers/lessons/8-leader/dominator/)

실수한 부분 2가지 🤦🏻‍♀️

1. 빈 배열이 input으로 들어올 수 있다. (non-empty 반드시 체크하기)
2. Dominator은 절반보다 **많은** (같으면 안됨) 빈도수를 가져야 한다.

collections.Counter 모듈을 이용해서 풀었다.

```python
import collections

def solution(A):
    if len(A) == 0:
        return -1
    c = collections.Counter(A)
    most_common = c.most_common(1)[0]
    if most_common[1] <= len(A)/2:
        return -1
    else:
        return A.index(most_common[0]
```



# [EquiLeader](https://app.codility.com/programmers/lessons/8-leader/equi_leader/)

```python
import collections

def solution(A):
    if len(A) == 0:
        return -1
    c = collections.Counter(A)
    most_common = c.most_common(1)[0]
    #(1)
    if most_common[1] <= len(A)/2:
        return 0
    count = 0
    answer = 0
    for i in range(0,len(A)):
        if A[i] == most_common[0]:
            count +=1
        if count > (i+1)/2 and most_common[1]-count > (len(A)-(i+1))/2:
            answer += 1
    return answer
```

앞에서 Dominator 문제를 풀어서 비교적 수월하게 풀 수 있었다.

먼저 Leader을 찾고, Learder이 없으면 바로 0을 리턴한다.

만약 Leader이 있다면, 앞에서부터 leader이 나올때마다 count를 올려가며 해당 idx 기준으로 쪼갰을 때 여전히 왼쪽, 오른쪽 구간의 리더가 동일한지 파악한다.

시간복잡도는 O(N).