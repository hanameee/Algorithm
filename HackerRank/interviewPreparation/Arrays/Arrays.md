# Arrays

## New Year Chaos

[문제 URL]([https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays](https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=arrays))

처음에는 단순

**Bribe 당한 입장에서 몇 명에 의해 제낌 당했는가** 로 구하는 것이 포인트이다. A가 B를 Bribe 했다고 가정하면, A가 있을 수 있는 최고로 앞 위치는 B의 원래 위치 - 1 이다.

왜냐면 문제에 한 사람당 최고로 Bribe 할 수 있는 사람 수는 2명이라는 조건이 있기 때문!

왜일까? 🤔

Bribe 한 애는 

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

