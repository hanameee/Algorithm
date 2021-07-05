# [41] First Missing Positive

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | Easy Medium **Hard**             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 30분                          |
| 시간복잡도  | O(N)                             |

## Result

![41](41.png)

## Solving

~~sort를 해버리고 풀어서 그런가... hard 치고 이상하게 빨리 풀었다. 이 문제가 hard인 이유가 있을텐데...🤨 sort를 쓰면 안되는 문제인가..?~~

discussion을 좀 봐야겠다.

## Source

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        needed_next = 1
        for num in nums:
            if num == needed_next:
                needed_next += 1
            if num > needed_next:
                return needed_next
        return needed_next
```

## Solution

⚠️ **constant extra space, O(n)** 라는 조건이 있었다. 즉, 공간 복잡도가 **O(1)**, 시간 복잡도가 **O(N)** 이어야하므로 sort를 사용할 수 없다. (p.s. python sort의 space complexity는 worst O(N), best O(N) 이고 time complexity는 O(𝑛log2𝑛)이다) Leetcode가 관대해서 sort 한 코드도 accept 해준거지, 이렇게 풀라고 낸 문제가 아니였다.

이 문제를 풀 때 중요한 아이디어는, 만약 missing integer이 있다면 그 숫자는 반드시 [1...n] 사이에 있어야 한다는 점이다! (n은 nums의 길이)

이 가정으로 인해 [1...n] 의 고정된 해시 테이블만 가지고도 first missing positive를 찾아낼 수 있다.

```js
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        arr = [False for _ in range(n+1)]
        for num in nums:
            if num < 0 or num > n:
                continue
            else:
                arr[num] = True
        for i in range(1,n+1):
            if not arr[i]:
                return i
        return n+1
```
