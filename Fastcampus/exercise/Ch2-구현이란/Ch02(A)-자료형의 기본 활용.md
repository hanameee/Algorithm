# Ch 02(A) - 자료형의 기본 활용

## 15969. 행복

먼저 **예제 입력 예시**를 보고 지문을 읽는 것을 추천한다. 이해가 더 잘됨!
map에서 list 로 변환해주는 것 잊지 말기.

```python
n = int(input())
data = list(map(int, input().split()))
print(max(data) - min(data))
```

## 10539. 수빈이와 수열

`join` 까먹지 말기.

```python
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
cumm = 0
for i in range(n):
    data[i] = data[i]*(i+1)-cumm
    cumm += data[i]
print((" ").join(list(map(str, data))))
```

```python
for i in A:
  print(i, end=' ')
```

위 처럼 출력하는 것도 가능.

`append` 를 하는 것 보다는, 배열을 미리 선언해두고 값을 바꿔주는 것이 더 빠르다.

## 17269. 이름궁합 테스트 - list comprehension, format

```python
import sys
input = sys.stdin.readline

num = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 2,
    "E": 4,
    "F": 3,
    "G": 1,
    "H": 3,
    "I": 1,
    "J": 1,
    "K": 3,
    "L": 1,
    "M": 3,
    "N": 2,
    "O": 1,
    "P": 2,
    "Q": 2,
    "R": 2,
    "S": 1,
    "T": 2,
    "U": 1,
    "V": 1,
    "W": 1,
    "X": 2,
    "Y": 2,
    "Z": 1,
}

n, m = map(int, input().split())
a, b = input().split()
min_len = min(len(a), len(b))
num_arr = [0]*(min_len*2)
for i in range(min_len*2):
    if i % 2 == 0:
        num_arr[i] = num[a[int(i//2)]]
    else:
        num_arr[i] = num[b[int(i//2)]]
if len(a) < len(b):
    for i in range(min_len, len(b)):
        num_arr.append(num[b[i]])
else:
    for i in range(min_len, len(a)):
        num_arr.append(num[a[i]])

while len(num_arr) > 2:
    new_arr = []
    for i in range(0, len(num_arr)-1):
        new_num = (num_arr[i]+num_arr[i+1]) % 10
        new_arr.append(new_num)
    num_arr = new_arr

num_arr = list(map(str, num_arr))
if num_arr[0] == "0":
    print(num_arr[1]+"%")
else:
    print(num_arr[0]+num_arr[1]+"%")
```

`정답 코드`

괜히 복잡하게 한 듯

```python
n,m = map(int, input().split())
a,b = input().split()
alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
AB = ''
# n,m 중 짧은 길이로 맞춰준다
min_len = min(n,m)
for i in range(min_len):
  # 요렇게 해주면 되는군... 머쓱...
  AB += A[i] + B[i]
# 남은 문자열 처리 (자동으로 빈 문자열을 반환하게 되기에)
AB += A[min_len:] + B[min_len:]
# 숫자로 변환해주기
lst = [alp[ord(i)-'A'] for i in AB]
# 앞의 값을 둘 씩 더해주기 (얼마나? 한번 할때마다 1씩 줄어들고, 길이를 2만큼 남겨야 한다)
for i in range(N+M-2):
  for j in range(N+M-1-i):
    lst[j] += lst[j+1]
    lst %= 10
print("{}%".format(lst[0] % 10*10 + list[1]%10))
```

`list comprehension⭐️` 

```python
lst = [alp[ord(i)-'A'] for i in AB]
```

AB에 있는 문자열들에 대해, 숫자와 매칭해주기
**ord(i)-'A' 를 하면 'A'는 0부터 인덱스가 시작하는 값**이 된다!

`출력할 때 format 사용하기`

```python
print("{}%".format(lst[0] % 10*10 + list[1]%10))
```

같은 lst에 값만 바꿔주고 나중에는 lst[0], lst[1] 만 사용함으로써 최대한 객체 생성을 지양

## 17389. 보너스 점수 - enumerate 사용법

```python
import sys
input = sys.stdin.readline

n = int(input())
answer = input()
bonus_point = 0
total_point = 0
for i in range(n):
    if answer[i] == "O":
        total_point += i+1+bonus_point
        bonus_point += 1
    else:
        bonus_point = 0
print(total_point)
```

`정답 코드`

enumerate 사용법 - 반복문 사용 시 몇 번째 반복문인지 확인할 수 있다. 인덱스 번호와 컬렉션의 원소를 tupel 형태로 반환한다.

```python
t = [1, 5, 7, 33, 39, 52]
for idx, p in enumerate(t):
  print(idx, p)
```

```python
n,s = input(), input()
# 튜플을 이렇게 사용한다
score, bonus = 0,0 
for idx, OX in enumerate(S):
  if OX = "O":
    score, bonus = score + idx+1+bonus, bonus+1
  else:
    bonus = 0
```

