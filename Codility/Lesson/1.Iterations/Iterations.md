## 1. BinaryGap

```python
def solution(n):
    binary_arr = []
    # (1)
    while n != 0:
        binary_arr.append(n % 2)
        n = n//2
    max_gap = 0
    cumm_sum = 0
    gap = 0
    for item in binary_arr:
      	# (3)
        if cumm_sum == 1 and not item:
            gap += 1
        else:
          	# (2)
            cumm_sum += item
        if cumm_sum == 2:
            cumm_sum = 1
            max_gap = max(gap, max_gap)
            gap = 0
    return max_gap
```

누적합을 더했을 때 2이면 100..001 로 안에 binaryGap이 생긴 형태임에 착안했다.😎

(1) 먼저 binary를 구해 한 숫자씩 binary_arr에 넣어준다. (앞뒤가 바뀌어도 상관 없으므로 궂이 appendleft를 해주지 않아도 됨. deque를 사용하면 앞뒤 삽입 시간복잡도는 동일)

(2) binary_arr를 돌면서 누적합을 더하고,

(3) 누적합이 1인데 현재 숫자가 0이라면 이는 gap이므로 현재 gap에 1을 더해준다.

(4) 누적합이 2가 되면 max_gap을 업데이트해주고 누적합을 1로, gap을 0으로 업데이트 한다.



조심할 점: 00001 이렇게 양쪽이 1로 닫히지 않은 경우가 있을 수 있으므로, gap 길이를 연장할 땐 반드시 누적합이 1인지 확인해야 한다.

