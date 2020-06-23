# Arrays

## New Year Chaos

[문제 URL]([https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays](https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=arrays))

처음에는 단순하게 "원래 위치에서 얼마나 차이나는지를 구하면 되는거 아니야?" 라고 생각했는데, 응 아니야.

**Bribe 당한 입장에서 몇 명에 의해 제낌 당했는가** 로 구하는 것이 포인트이다. A가 B를 Bribe 했다고 가정하면, A가 있을 수 있는 최고 앞 위치는 B의 원래 위치 - 1 이다.

왜냐면 문제에 한 사람당 최고로 Bribe 할 수 있는 사람 수는 2명이라는 조건이 있기 때문!

```python
def minimumBribes(q):
    result = 0
    for idx, num in enumerate(q):
        if num - 3 > idx:
            return "Too chaotic"
        for i in range(max(num-2, 0), idx):
            if q[i] > num:
                result += 1
    return result
```

따라서 모든 사람들에 대해, `num-2` (자신의 원래 위치 - 1) 와 `idx` (자신의 현재 위치 - 미포함) 사이의 범위에서 자신을 bribe 한 사람 수를 세면 된다.

## Minimum Swaps 2

[문제 URL]([https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays](https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=arrays))

배열의 맨 앞부터, **자신이 원래 위치까지 swap 되기까지 거쳐야 하는 노드들**을 세고, 그 노드들은 다 ck 배열에 체크해둔다.

[예제 1]

예를 들어, `1 4 3 2 5` 라는 배열이 있다면

- 1은 제 위치에 있으므로 넘어간다
- 4는 현재 2가 있는 자리로, 2는 현재 4가 있는 자리로 : 1개의 swap (2-4)
- 3은 제 위치에 있으므로 넘어간다
- 2는 아까 4에서 ck 되었으므로 넘어간다
- 5는 제 위치에 있으므로 넘어간다

따라서 총 1개의 swap이 이루어진다.

[예시 2]

`1 3 5 2 4 6 7`

- 1은 제 위치에 있으므로 넘어간다
- 3은 현재 5가 있는 자리로, 5는 현재 4가 있는 자리로, 4는 현재 2가 있는 자리로, 2는 현재 3이 있는 자리로 : 3개의 swap (3-5, 5-4, 4-2)
- 5,2,4는 아까 3에서 ck 되었으므로 넘어간다
- 6,7은 제 위치에 있으므로 넘어간다

따라서 총 3개의 swap이 이루어진다

```python
def minimumSwaps(arr):
    arr = [num-1 for num in arr]
    idx_arr = [0 for i in range(len(arr))]
    ck = [0 for i in range(len(arr))]
    for idx, num in enumerate(arr):
        idx_arr[num] = idx
    swaps = 0
    for idx, num in enumerate(arr):
        if idx == num or ck[idx]:
            continue
        while num != idx:
            idx = idx_arr[idx]
            ck[idx] = 1
            swaps += 1
    return swaps
```

## Array Manipulation

Brute Force로 그대로 구현하는것 말고, O(n) 에 풀 수 있는 방법이 있을 터인데, 생각이 안났다.

그래서 discussion 을 봤다! (당당)

정말 브릴리언트한✨ 풀이가 있더라.

```python
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for q in queries:
        arr[q[0]-1] += q[2]
        arr[q[1]] -= q[2]
    answer = 0
    cumulative_sum = 0
    for value in arr:
        cumulative_sum += value
        answer = max(answer, cumulative_sum)
    return answer
```

`a,b,v` 쿼리가 있을 때, 끝 점의 값만 기록하는 것이다.

a에는 v를, b+1에는 -v를 기록한다. (정확하게 말하면 n만큼의 배열을 0으로 초기화한 뒤 v, -v만큼 더하고 빼주는 것) 

이렇게 기록하면, 누적합을 했을 때 가장 큰 누적합이 최대 값임을 알 수 있다.

1,5,3 과 3,6,2 query가 있다고 해보자.

1에 3을 기록하고, 6에 -3을 기록한다.

3에 2를 기록하고, 7에 -2를 기록한다.

그러면 누적합은 `3 3 5 5 5 2 0` 이 되고, 이는 모든 값들을 합친 결과와 동일하다. 일일히 모든 index를 계산하지 않아도 누적합의 원리로 최댓값을 구할 수 있는 것.