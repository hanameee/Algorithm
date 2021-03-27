# [53] Maximum Subarray

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | **Easy** Medium Hard             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |

## Solving

O(n)으로 어떻게 풀지 고민하다가 누적합으로 풀었는데, ac 맞기 전까지 여러번 틀렸을뿐더러 좀...이상하게 푼 것 같다.

기본적으로 누적합을 다 구하되, 누적합 간의 차가 최댓값이 나오는 경우를 구하려고 했다.

| 숫자   | -2   | 1    | -3            | 4    | -1   | 2    | 1            | -5   | 4    |
| ------ | ---- | ---- | ------------- | ---- | ---- | ---- | ------------ | ---- | ---- |
| 누적합 | -2   | -1   | -**4** (최소) | 0    | -1   | 1    | **2** (최대) | -3   | 1    |

위 예제에서는 2-(-4)가 6으로 최대 subarray에 해당한다. (4~1까지의 합)

acc_num에 누적합을 저장하고, max_value에는 (현재 누적합 - 현재까지의 최소 누적합, 현재 누적합, 예전 최대값) 중 최대값을 저장했다. 마지막에는 최소 누적합인 min_value를 업데이트 해줬다.

차의 최댓값을 구하는게 아니라 그냥 누적합에 포함할 지 안할지를 생각했으면 됐는데...괜히 복잡하게 생각한듯.

## Source

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc_num = nums[0]
        min_value = nums[0]
        max_value = nums[0]
        for num in nums[1:]:
            acc_num += num
            max_value = max(acc_num - min_value, acc_num, max_value)
            if acc_num < min_value:
                min_value = acc_num
        return max_value
```

푼  후에 답지 보니까, DP로 푸는 방법과 누적합으로 푸는 방법 2개가 있는 것 같아 정리해둔다.

**[누적합으로 푸는 방법]**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = -math.inf
        for num in nums:
          cur_sum += num
          max_sum = max(cur_sum, max_sum)
          cur_sum = max(cur_sum, 0)
        return max_sum
```

앞에서부터 하나씩 누적합을 구해가면서, 현재까지의 최대 누적합을 max_sum에 저장해둔다.

만약 현재 단계의 누적합이 0보다 작다면, 그 숫자는 안더하느니만 못하므로 cur_sum을 0으로 해준다. (그 전의 숫자는 더하지 않는 것)

**[DP로 푸는 방법]**

풀이로 보니까 허무하게 쉽게 느껴진다...DP는 항상 알고 나면 쉽다...제일 명확하고 깔끔한 방법인 것 같다.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx], dp[idx-1]+nums[idx])
        return max(dp)
```

Maximum subarray를 구하는 과정은 결국 부분합을 어디부터 시작해서, 어디까지 더할지이다. nums[idx]의 입장에서 생각해봤을때 (1) 기존 subarray에 자기 자신을 더하기 (2) 자기부터 새로운 subarray 시작하기 이렇게 2가지 선택지가 있다.

그래서 점화식이

```python
dp[idx] = max(nums[idx], dp[idx-1]+nums[idx]) 
```

로 나오는 것! 

dp[idx] 배열은 **num[idx]를 포함하는** 최대 부분합에 해당한다.