# [MaxNonoverlappingSegments](https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/)

```python
import heapq

def solution(A, B):
    q = []
    for i in range(len(A)):
        heapq.heappush(q, [B[i],A[i]])
    answer = 0
    end = -1
    while q:
        cur_end, cur_start =  heapq.heappop(q)
        if cur_start > end:
            answer +=1
            end = cur_end
    return answer
```

히든테케 없는 정직한 힙큐 문제. End time 기준으로 minHeap 사용하면 된다.

지금 꺼낸 애의 Start time이 누적 end time보다 느리면 overlap 하지 않는 것이므로 정답에 1 추가해주고, 누적 end time 업데이트.

q가 빌때까지 반복.



# [TieRopes](https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/)

```python
from collections import deque

def solution(K, A):
    answer = 0
    A = deque(A)
    while A:
        cur = A.popleft()
        if cur>=K:
            answer +=1
            continue
        else:
            while A:
                cur2 = A.popleft()
                cur += cur2
                if cur>=K:
                    answer += 1
                    break
    return answer
```

여러번 틀렸다 :D... **adjacent** 로프를 엮을 수 있다는 조건을 못보고 계속 힙큐로 풀었다...? :D....하하하하! 조건을 잘 읽자!

인접한 로프만 엮을 수 있으므로, deque를 사용해 앞부터 pop하면서 deque가 남아있고 & 엮은 로프가 K이상이 될때까지 합치는 작업을 반복한다.