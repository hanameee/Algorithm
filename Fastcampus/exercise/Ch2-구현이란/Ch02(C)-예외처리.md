# Ch 02(C) - 예외처리

코딩테스트에서 가장 빈출되는 유형은 **BFS, DFS, 전수조사, 그리고 하드한 조건문이자 반복문**이다. 왜냐? 구현 능력을 보기 위해서임.

문제가 준 까다로운 조건이 많다. 그럼 이런 까다로운 조건들을 어떤 식으로 처리할까?

## 1. 논리 연산자 / 비트 연산자 잘 활용하기

### 논리 연산자

깊게 반복문이 들어가지 않게 작성해야 한다

🚫 

```python
a,b = 10,20
if a > b:
  if a % 10 == 0:
    print(a)
```

✅ 

```python
a,b = 10,20
if a > b and a % 10 == 0:
    print(a)
```

and, or, not을 잘 활용해서 반복문이 깊어지지 않게 작성하기.

### 비트 연산자

shift 연산자 `<<`, and 연산자 `&` , or 연산자 `|` , xor 연산자 `^`  를 알고 있으면 좋다.

## 2. 상태를 나타내는 자료 활용하기

소수인지 아닌지를 체크해야 한다고 해보자

```python
n = 71
# flag나 ck등의 변수로 상태를 나타내는 자료를 활용할 것!
ck = 0
for i in range(2,n):
  if n%i ==0:
    print("not prime")
    ck = 1
    break
if ck:
  print("prime")
```

단순 단일 변수 flag 말고,
배열에서 어떤 것을 사용했다 안사용했다를 나타내는 ck 배열이 될 수도 있고,
이 문자열이 포함되었나 안되었나를 나타내는 set 나 dictionary가 될 수도 있다.

## 3. 나눠서 진행하기

만약 한 값이 아니라 어떤 범위의 수에 대해 소수인지 아닌지를 체크해야 할 때는?

```python
def isPrime(n):
  for i in range(2,n):
    if n%i ==0:
      return False
  return True

for n in range(10,100):
  if isPrime(n):
    print("{} is Prime".format(n))
  else:
    print("not prime")
```

아예 조건 체크하는 코드를 함수로 따로 분리하면 코드가 간결해진다!

DFS,BFS에서 2,3차원 배열에서 탐색을 하는 경우가 많은데, 이 때 

```python
# 0부터 n까지, 0부터 m까지의 배열 속에서 a,b가 범위에 있나 체크할 때
def isRange(a,b,n,m):
  return 0<=a<n and 0<=b<m
```

위와 같이 분리하면 좀 더 코드가 간결해질 수 있다.

## 4. 여러 자료구조와 메서드, 함수 활용하기

예제1: Palindrom 을 체크할 때

```python
for idx in S:
  if S[idx] != S[len(S)-idx-1]:
    print('not palin')
```

이렇게 커스텀 함수를 작성할 수도 있지만, 시간복잡도가 여유롭다면

```python
if S == S[::-1]:
  print("isPalin")
```

위와 같이 파이썬의 특징을 활용해서 작성할 수도 있다.

`S[::-1]` 이란? S와 S를 복사한 배열을 역으로 읽었을 때 어떻게 되느냐를 나타내는 코드이다.
왜냐면 파이썬에서 `[a:b:c]` 는 a번 인덱스부터 b번 인덱스까지 c의 간격으로 출력해주는 것인데, c가 -1일 때, a번 인덱스가 마지막 인덱스라면 생략할 수 있다. b는 초기값인 0으로 설정된다. 따라서 `[::-1]` 은 배열을 역순으로 출력해주는 것이 된다!

예제2: 배열에 있는 모든 값이 다른지를 체크할 때

```python
def isUnique(lst):
  return len(lst) == len(set(lst))
```

리스트와, 리스트를 셋으로 만든게 길이가 같은지를 보면 된다.

## 5. 미리 처리한 케이스와 처리할 케이스 정리하기

미리 조건을 다 작성하고, 하나 하나씩 조건을 처리한 코드를 작성해주면 실수를 할 확률이 낮아진다. 

- 문제에서 나온 **예제 케이스**는 꼭 테스트 해봐야 한다
- **최소/최대 케이스** - n이 0부터 10000까지면, 0와 10000은 꼭 체크해야 한다. 대부분 Index 에러는 최소/최대 케이스에서 나온다.
- 예외 케이스 - 조건 A는 없고, 조건 B는 있는. 조건 B는 없고, 조건 A는 없는. 두 조건 모두 있는.
- 랜덤 케이스 만들기

---

## 2480. 주사위 세개

정렬을 하고 시작하면, 같은 주사위가 2개일 경우에 고려해야 할 복잡도를 줄일 수 있다. **정렬한다면 들어가면 무조건 가운데에 있는 수가 같은 수일 테니까!** 

```python
lst = sorted(list(map(int, input().split())))
```



## 2484. 주사위 네개

구현이 복잡한 문제. 세번 틀렸다 쉬익쉬익
**set은 딕셔너리처럼 순서가 없기 때문에 index로 접근할 수 없음**에 주의할 것!

```python
def money():
  lst = sorted(list(map(int,input().split())))
  # elif 안쓰고 여러개의 if로 early return을 해주기
  if len(set(lst)) == 1:
    return lst[0] * 5000 + 50000
  if len(set(lst)) == 2:
    if lst[1] == lst[2]: # 두번째와 세번째가 같다는 것은 1:3이거나 3:1이라는 것
      return 10000 + lst[1]*1000
    else:
      return 2000 + (lst[1]+lst[2])*500
  for i in range(3):
    # 같은 눈이 있는 경우
    if lst[i] == lst[i+1]:
      return 1000 + lst[i]*100
 	return lst[-1]*100
n = int(input())
print(max(money() for i in range(n)))
```

예외처리 잘 하는거 중요합니다아~



## 16675. 두개의 손

한 사람이 똑같은 걸 냈을 때, 다른 사람이 그걸 이기는 패를 가지고 있다면 승부가 난다.
가위바위보, 즉 A가 B를 이기고 B가 C를 이기고 C가 A를 이기는 삼각형 구조는 **수학에서의 % 연산과 상당히 비슷**하다.

내가 만약 가위를 가지고 있으면, 상대방이 이기려면 바위를 가지고 있어야 한다. 이를 다 숫자로 나타내보면

```python
0 2
1 0
2 1
```

즉, **내것보다 +2한 것의 %3 한 것이 상대방에 있다면** 상대방이 이기는 것.



tuple comprehension**을 사용한 것 같다. (find를 사용해도 되고, index를 사용해도 된다.)

```python
ml, mr, tl, tr = ('SPR'.index(i) for i in input().split())
```

로 입력을 받으면, **S는 0, P는 1, R은 2로 매핑**되게 한 것!

언제 승부가 결정 나냐? 한 사람이 같은 걸 가지고 있는데, 다른 사람이 이기는 패를 가지고 있을 때!

```python
ml, mr, tl, tr = ('SPR'.index(i) for i in input().split())
if ml == mr and (ml+2)%3 in [tl,tr]:
  print("TK")
elif tl == tr and (tl+2)%3 in [ml, mr]:
  print("MS")
else:
  print("?")
```

이렇게 간단하게 풀 수 있다니 !_! 가위바위보를 012로 매핑해주고, 모듈러 연산을 통해 한번에 처리해줬다.

index,find를 사용해서 comprehension을 사용하기, cycle이 있는 경우 모듈러 연산을 활용하기.

`index, find`

문자열에서 index와 find는 거의 같은 역할을 한다. find는 문자열에서 찾는게 있으면 첫번째로 발견되는 인덱스를, 없으면 -1을 리턴. index는 없으면 에러 뿜으니 사용하지 말자. 

find는 문자열에서만 사용 가능한 것 과는 달리, 리스트에서는 index만 사용할 수 있다. 하지만 없으면 에러다!

## 17413. 단어 뒤집기 2

[문자열 거꾸로 출력하기](https://itholic.github.io/python-reverse-string/)

파싱하는 문제! 연습이 필요하다. 나는 index를 바꿔가며 result string에 concat 하는 식으로 했는데, 정답 풀이는 for문을 돌며 처리했다.

내 방법도 좋은 풀이라고 하심 '~'

`내 풀이`

```python
import sys
input = sys.stdin.readline

s = input()
result = ""
l = 0
r = 0

while len(s):
    # 지금 보고있는 문자열이 태그일때
    if s[0] == "<":
        tag_s = ''.join(s[s.find("<"):s.find(">")+1])
        result += tag_s
        s = s[s.find(">")+1:].strip()
    # 지금 보고있는 문자열이 태그가 아닐 때
    else:
        # 앞으로도 태그가 없을 때
        if s.find("<") == -1:
            reversed_s = list(s.split())
            for i in range(len(reversed_s)):
                reversed_s[i] = ''.join(reversed(reversed_s[i]))
            result += ' '.join(reversed_s)
            s = []
        else:
            cur_s = s[:s.find("<")]
            reversed_s = list(cur_s.split())
            for i in range(len(reversed_s)):
                reversed_s[i] = ''.join(reversed(reversed_s[i]))
            result += ' '.join(reversed_s)
            s = s[s.find("<"):].strip()
print(result)
```

`정답 풀이`

```python
s,tmp = input(),""
# 꺽쇄 안에 있으면 ck를 True로
ck = False
# 4가지 경우로 나눌 수 있다. 공백, 여는 태그, 닫는 태그, 그 외
for i in S:
  if i == ' ':
    if not ck:
      print(tmp[::-1],end=" ")
      tmp = "" # 이미 출력해준 애들은 버퍼를 지운다는 느낌으로
  elif i in '<':
    ck = True
    print(tmp[::-1] + "<",end="")
    tmp = ""
  elif i in '>':
    ck = False
    print(">", end="")
  else: # 알파벳과 숫자
    if ck:
      print(i, end="")
    else:
      tmp += i
print(tmp[::-1],end=" ")
```