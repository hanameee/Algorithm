# [17] Kth Largest Element in a Stream

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | **Easy** Medium Hard             |
| 체감 난이도 | **Easy** Medium Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 15분                          |
| 시간복잡도  | O(n)                             |

## Result

![image-20210503001005683](image-20210503001005683.png)

## Solving

그냥 하라는 대로 구현했다. 최초 init때 nums를 정렬하고, 이후부터는 이진탐색으로 val을 순서에 맞게 insert 하고 -k 번째 원소 리턴하도록!

## Source

```python
from bisect import bisect_left, bisect_right

class KthLargest(object):
    K = 0
    nums_arr = []

    def __init__(self, k, nums):
        self.K = k
        self.nums_arr = sorted(nums)

    def add(self, val):
        self.nums_arr.insert(bisect_left(self.nums_arr, val), val)
        return self.nums_arr[-self.K]
```
