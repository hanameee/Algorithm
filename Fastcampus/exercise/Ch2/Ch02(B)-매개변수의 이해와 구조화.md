# Ch 02(B) - 매개변수의 이해와 구조화

## 함수의 이름과 역할

-  코테에서는 궂이 모듈화를 꼼꼼하게 할 필요는 없다. 그러나, 코드가 길어질 것 같다면 (예 - 반복문이나 조건문이 4개 이상 될 것 같다면) 함수로 분리하기.
-  함수명은 역할을 알아볼 수 있도록 확실하게.
- **반환 값**을 미리 지정하는 것이 명확하고 좋다.


## 함수의 매개변수

- 반환 값과 마찬가지로 **함수의 매개변수** 역시 미리 적어주는 것이 중요하다

  ```python
  # money_sum : 돈의 합을 출력
  # N: 사람수, money_arr : 사람의 돈
  def money_sum(N, money_arr):
    ret = 0
    for i in range(N):
      ret += money_arr[i]
   	return ret
  ```
  
- 복잡하거나 까먹기 쉬운 내용은 주석으로 함수/매개변수 역할을 간략하게 적어두면 도움이 된다

- **필요한 것**과 **편한 것** (없어도 되지만 있으면 편한)을 넘기기

## Container(자료형) 의 역할

- 자료형에 따른 본인만의 container의 설정과 이해
  - Tuple: 위치(index)에 따른 의미
  - Set: 포함 여부의 의미
  - List: index와 원소의 관계
  - Dict: key와 value의 관계

## Container(자료형) 의 분할

- 2차원 배열을 만드는 것 보다, 서로 다른 1차원 배열을 2개 만드는 것이 나을 수도 있다. 정답은 없고, 그때 그때 더 헷갈리지 않는 것을 택하면 됨.

---

## 1920. 수 찾기 - dictonary 사용, get 메서드 사용

정해는 배열을 정렬한 뒤, 이분 탐색을 이용해서 푸는 것임.
하지만 이 문제는 파이썬의 장점을 활용! 해쉬를 이용한 내장 dictionary 자료구조를 이용하면 더 빠르게 풀 수 있음.

```python
# dictonary comprehension 사용
n,a = int(input()), {i:1 for i in map(int, input().split())}
m = input()
for i in list(map(input().split())):
  print(a.get(i,0))
```

파이썬의 dictonary는 없는 값을 출력해주지 않는다. get이라는 메서드는 등록 안된 키 값이 있다면 default 값을 출력해준다.

`a.get(i,0)` : a에서 i라는 키가 있다면 i의 값을, 없다면 default 값인 0을 출력해준다.

+) 참고 - 이분 탐색 풀이는 다음과 같다

```python
import sys
input = sys.stdin.readline

n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()
m = int(input())
m_data = list(map(int, input().split()))


# arr = 대상을 찾는 배열 target = 찾는 숫자
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
        else:
            return 1
    return 0


for target in m_data:
    print(binary_search(n_data, target))
```

Binary_search는 left/right를 return 하는게 아니다. 그건 quick sort고...!
Binary_search는 index를 좁혀나가며 low>high이 될 때 까지반복하는 것.



## 16165. 걸그룹 마스터 준석이

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gg_dict = {}
for _ in range(n):
    gg_name = input().strip()
    gg_dict[gg_name] = []
    gg_member_num = int(input())
    for _ in range(gg_member_num):
        gg_dict[gg_name].append(input().strip())

for _ in range(m):
    quiz_name = input().strip()
    quiz_type = int(input())
    if not quiz_type:
        gg_dict[quiz_name].sort()
        for member in gg_dict[quiz_name]:
            print(member)
    else:
        for gg in gg_dict.keys():
            if quiz_name in gg_dict[gg]:
                print(gg)
```

`정답 코드`

team_mem 이랑 mem_team 딕셔너리 2개를 만들면 더 빠르겠군!

```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 요건 튜플 사용한 것임
team_mem, mem_team = {},{}

for i in range(n):
  team_name, mem_num = input(), int(input())
  # value 값을 list 로!
  team_mem[team_name] = []
  for j in range(mem_num):
    name = input()
    # mem_num 마다 team_mem과 mem_team에 다 데이터를 넣어준다
    team_mem[team_name].append(name)
    mem_team[name] = team_name
```

딕셔너리와 리스트를 연결해서 쓰면 편하다.



## 17224. APC는 왜 서브태스크 대회가 되었을까?

```python
import sys
input = sys.stdin.readline
n, l, k = map(int, input().split())
prob = []
score = 0
for _ in range(n):
    easy, hard = map(int, input().split())
    prob.append((easy, hard))
prob.sort(key=lambda x: x[1])
solved_prob = [0]*n
for i in range(n):
    if k:
        # 어려운 문제 해결 가능하면
        if l >= prob[i][1]:
            score += 140
            solved_prob[i] = 1
            k -= 1

for i in range(n):
    if k:
        # 안푼 쉬운 문제 해결 가능하면
        if l >= prob[i][0] and solved_prob[i] == 0:
            score += 100
            k -= 1

print(score)
```

`답안 코드`

easy 문제, hard 문제 풀 수 있는 개수 각각 저장해두고 k와 비교해서 출력하기.

```python
n,l,k = map(int, input().split())
easy, hard = 0, 0
for i in ragne(N):
  sub1, sub2 = map(int,input().split())
  if sub2 <= l:
    hard += 1
  elif sub1 <= l:
    easy += 1
# hard 문제
score = min(k, hard) * 140
# easy 문제
if hard < k:
  score += max(k-hard, easy) * 100
print(score)
```



## 9037. The candy war

n이 별로 크지 않기 때문에 단순한 구현 문제이다.

```python
import sys
input = sys.stdin.readline

test_case = int(input())


def is_same(arr):
    value = arr[0]
    for item in arr[1:]:
        if item != value:
            return False
    return True


for _ in range(test_case):
    cycle = 0
    n = int(input())
    candies = list(map(int, input().split()))
    for i in range(n):
        if candies[i] % 2 == 1:
            candies[i] += 1
    while True:
        if is_same(candies):
            print(cycle)
            break
        new_candies = [0]*n
        for i in range(n):
            new_candies[i] = (candies[i-1]//2)+(candies[i]//2)
            if new_candies[i] % 2 == 1:
                new_candies[i] += 1
        candies = new_candies
        cycle += 1
```

모범 답안은 check, teacher, process 로 함수를 나눠서 아래처럼 작성했음

```python
def ck(N, lst):
    for i in range(N):
        if lst[i] % 2 == 1: lst[i] += 1
        if lst[0] != lst[i]: return False
    return True


def teacher(N, lst):
    lst_tmp = lst[:]
    for idx, candy in enumerate(lst):
        lst[idx] = (lst[idx]+1)//2
        lst_tmp[(idx+1) % N] = lst[idx]
    for i in range(N):
        lst[i] += lst_tmp[i]
    return lst


def process():
    N, lst = int(input()), list(map(int, input().split()))
    cnt = 0
    while not ck(N, lst):
        cnt += 1
        lst = teacher(N, lst)
    print(cnt)


for i in range(int(input())): process()
```



## 16769. Mixing milk

```python
milk_data = []
for i in range(3):
    c, m = map(int, input().split())
    milk_data.append([c, m])


def pour(source, target):
    s_c, s_m = source
    t_c, t_m = target
    # s_m가 t_c-t_m보다 같거나 작다면
    if s_m <= t_c-t_m:
        source[1] = 0
        target[1] = t_m+s_m
    else:
        source[1] -= t_c-t_m
        target[1] = t_c
    return (source, target)


for i in range(100):
    source = milk_data[i % 3]
    target = milk_data[(i+1) % 3]
    pour(source, target)

for data in milk_data:
    print(data[1])
```



## 1074. Z

풀어본 문제지만, 구조화를 연습하기에 아주 좋은 문제! 다시 풀어보고 강의를 볼 것.