# Week 1

## [number of 1 bits](https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/)

### 제출 답

unsigned integer **n**을 input으로 받고, n에 포함된 "1" bits의 갯수를 리턴하는 문제.

쉬운 문제인데 알고리즘 하도 오랜만에 풀어서 문법부터 기억이 안났다. 진법과 관련된 문법이 있었던걸로 기억하지만 일단 그냥 고전적으로 나머지 더해버렸다.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n != 0:
            div, mod = divmod(n,2)
            answer += mod
            n = div
        return answer
```

약간 구닥다리같아보이는 방법이다. 후후

### 모범 답 #1

**비트마스크** 쓰기에 딱인 문제. mask 1과 특정 자릿수와의 logical AND를 하면 그 자릿수가 1인지 아닌지를 알 수 있다.

input은 32비트. 마지막 자릿수 ~ 첫번째 자릿수까지 1과 `&`를 해보면 된다. 자릿수를 이동할 때는 시프트 연산자를 이동하면 됨.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        mask = 1
        for i in range(0,32):
            if n & mask != 0:
                answer += 1
            mask <<= 1
        return answer
```

시간복잡도, 공간복잡도 모두 O(1)

### 모범 답 #2

모범 답 1을 좀 더 발전시켜보자. (좀 더 간결하고 살짝 빠르게)

모든 32비트를 다 체크하는 대신, least-significant 1-bit를 계속 flip (1 > 0) 해가면서 answer에 1씩 더하고, n이 0이 되는 순간 = 더 이상 1-bit이 없는 순간이므로 answer을 리턴하면 된다.

그럼 **least-significant 1-bit 어떻게 flip 할 것**인가가 중요해진다! n과 n-1을 `&` (bit-wise AND) 하는 것!

그 이유에 대해서는 LeetCode의 아래 기똥찬 사진으로 대체...

<img src="https://leetcode.com/media/original_images/191_Number_Of_Bits.png" alt="Number of 1 Bits" style="zoom:50%;" />

무튼 그래서 

AND-ing **n** and **n-1** flips the least-significant 1-bit to 0이라는 것!

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n != 0:
          answer += 1
          n &= (n-1)
        return answer
```

시간복잡도, 공간복잡도 모두 O(1)

### 꼼수 답 #3

아래 설명하겠지만 파이썬은 10진수를 2진수 문자열로 변환하는 방법이 있다. `bin` 연산자!

또, 문자열에서 특정 문자의 갯수를 세는 메소드도 있다. `count` 메소드!

요 두개를 결합하면 한줄로 풀 수가 있다.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
      bin(n).count('1')
```

파이썬은 오늘도 달달하다 ☺️

#### 참고) 파이썬의 비트 연산 [출처](https://dojang.io/mod/page/view.php?id=2460)

컴퓨터는 2진수를 사용하지! 파이썬에서 2진수를 다루는 방법에 대해 알아보자.

1) 10진수와 2진수 변환

- 10진수를 2진수로 변환할 때는 `bin`을 사용한다.

  ```python
  >>> bin(13) # 10진수 13을 2진수로 변환
  '0b1101'
  ```

- 2진수는 입력 즉시 10진수로 변환된다.

  ```python
  >>> 0b1101 # 코드에서 2진수를 직접 입력할 때는 맨 앞에 0b를 붙인다
  13
  ```

- 문자열 형태의 2진수는 int에 문자열과 2를 지정하여 10진수로 변환할 수 있다.

  ```python
  int('1101', 2) # 2진수로 된 문자열 1101을 10진수로 변환
  13
  ```

2) 비트 논리 연산자 사용하기

|        | 기호     |
| ------ | -------- |
| a & b  | 비트 AND |
| a \| b | 비트 OR  |
| a ^ b  | 비트 XOR |
| ~x     | 비트 NOT |

`13 & 9` 비트 연산의 결과는 아래와 같다.

<img src="https://dojang.io/pluginfile.php/14088/mod_page/content/4/047002.png" alt="img" style="zoom:50%;" />

3) 시프트 연산자 사용하기

시프트 연산자(`<<`, `>>`)는 비트의 위치를 이동시킨다.

```python
>>> 0b0011 << 2 # 비트를 왼쪽으로 2번 이동
12
>>> bin(12)
'0b1100'
```

참고로, 비트를 오른쪽으로 이동시켰을 때 1이 들어갈 공간이 없다면 1은 사라진다.