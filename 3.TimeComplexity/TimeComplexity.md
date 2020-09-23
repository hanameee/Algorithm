# Frogjmp

```python
import math

def solution(X, Y, D):
    return math.ceil((Y-X)/D)
```

간단한 문제.

# PermMissingElement

마지막 값, 마지막 값 조심!

```python
def solution(A):
    #(1)
    A.sort()
    for i in range(len(A)):
        #(2)
        if A[i] != i+1:
            return i+1
    #(3)
    return len(A)+1
```

(1) 배열 A를 정렬한다

(2) 정렬하다가 값이 idx+1인 친구가 있다면 즉시 리턴한다.

(3) 마지막까지 리턴이 안되었다면 이는 빈 값이 마지막 값임을 의미한다. - 처음에 이 로직 안넣어서 틀림.

테스트케이스로 **빈 배열**, 정답이 **양끝값**일 때를 꼭 테스트 해볼 것.

# TapeEquilibrium

```python
def solution(A):
    cumm = 0
    min_v = float('inf')
    sum_v = sum(A)
    for i in A[:-1]:
        cumm += i
        min_v = min(min_v, abs(sum_v-2*cumm))
    return min_v
```

코딜리티는 쉽다고 생각하고 생각없이 풀다가 기본적으로 3-4번은 다시 푸는 것 같다. 하하

O(N)에 풀 수 있는 문제다.

배열을 2개로 쪼개야 하는데, 가만히 규칙을 보면 배열을 2개로 쪼갠다고 했을 때 한쪽이 n이면, 나머지 한쪽은 sum(A)-n이다. 따라서 양쪽의 차이는 abs(sum(A)-n-n) = abs(sum(A)-2n) 이다.

n은 누적합이므로 A[0]부터 **A[n-2]** 까지 쭉 더해가면서 최소값을 업데이트 해주면 된다. 반드시 배열이 쪼개져야하므로 A[n-1]까지 고려하면 안되고 A[n-2]까지만 누적합을 구해야 함에 주의.