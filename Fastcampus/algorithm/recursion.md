# 재귀

함수 안에서 동일한 함수를 호출하는 형태.

## 1. 재귀 용법 (recursive call, 재귀 호출)

`팩토리얼 함수`

```python
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n


print(factorial(5))
```

- factorial(n) 은 n-1 번의 반복문을 호출한 것과 동일
- factorial 함수를 호출 할 때마다 지역변수 n이 생성됨
- 시간복잡도 공간복잡도 모두 O(n)



## 2. 재귀 호출의 일반적인 형태 (패턴)

### 일반적인 형태 1

```python
def function(입력):
  if 입력 > 일정값:
    return function(입력 - 1)
  else:
    return 일정값 
```

### 일반적인 형태 2

```python
def function(입력):
  if 입력 <= 일정값:
    return 일정값
  function(입력보다 작은 값)
  return 결과값
```



## 3. 재귀 호출은 스택의 전형적인 예

함수는 내부적으로 스택처럼 관리된다.
⚠️ 따라서 파이썬에서 재귀 함수는 깊이가 1000회 이하가 되어야 함. (스택 공간을 1000이하로 잡아두었기 때문에)



## 4. 재귀 용법을 활용한 프로그래밍 연습

### 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수

```python
import random

test_list = random.sample(range(100), 10)

# 일반적인 반복문 사용
def sum_all(data):
    result = 0
    for i in (data):
        result += i
    return result

# 재귀 함수 사용
def sum_all_recursive(data):
    if len(data) > 1:
      	# 재귀 호출하면서 전달하는 리스트의 인덱스 잘라내기
        return data[0] + sum_all_recursive(data[1:])
    else:
        return data[0]

      
print(sum_all(test_list))
print(sum_all_recursive(test_list))
```

### 회문(palindrome) 을 판별하는 함수

```python
# 리스트 슬라이싱 사용
def isPalindrome(data):
    flag = True
    for i in range(len(data)//2):
        if data[i] != data[-i-1]:
            return False
    return flag

# 재귀 함수 사용
def isPalindrome(data):
    if len(data) <= 1:
        return True
    # 맨앞과 맨 뒤 비교
    if data[0] == data[-1]:
      	# 같다면 맨 앞과 맨 뒤를 자른 데이터를 넘겨주어 계속해서 비교
        return isPalindrome(data[1:-1])
    else:
        return False
```

### 일정한 규칙에 따라 진행하는 함수

```python
def func(n):
    print(n)
    if n == 1:
        return n
    elif n % 2 == 0:
      	# 결과가 부동소수점으로 나오지 않게 int(n/2) 나 n//2 로 해주기!
        return func(n//2)
    else:
        return func(3*n+1)
```

### 규칙찾기 함수

```python
# 정수 4 를 1,2,3 의 조합으로 나타내는 방법은 총 7가지가 있다. 정수 n이 입력으로 주어졌을 때, n을 1,2,3의 합으로 나타낼 수 있는 방법의 수를 구하시오

def func(n):
    if n <= 2:
        return n
    if n == 3:
        return 4
    return func(n-3) + func(n-2) + func(n-1)
```

