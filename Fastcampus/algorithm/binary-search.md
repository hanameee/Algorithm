# 이진 탐색 (Binary Search)

자료구조 단원에서 여러 자료구조와 그 메서드들을 구현하면서 순차 탐색, 해쉬, 이진탐색트리(BST) 에서의 탐색을 배웠었다. 지금은 이진 탐색이라는 또 다른 방법을 익히는 것!

## 1. 이진 탐색이란?

탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법.
기본조건 : **정렬이 되어있는 상태**에 대해 적용할 수 있는 탐색 알고리즘.

## 2. 분할 정복 알고리즘과 이진 탐색

### 분할 정복 알고리즘 (divide and conquer) 복습

Divide : 문제를 하나 또는 둘 이상으로 나눈다
Conquer: 나눠진 문제가 충분히 작고 해결 가능하다면 해결, 그렇지 않으면 다시 나누기

분할 정복은 대부분 **재귀 용법**을 쓴다.

### 이진 탐색

Divide: 리스트를 2개의 서브 리스트로 나눈다
Conquer: 검색할 숫자와 중간값을 비교해서 해당하는 서브 리스트에서 다시 탐색한다

## 3. 코드로 이해하기

`내가 작성한 코드`

```python
import random
data_list = random.sample(range(15), 10)
print(data_list)

def binary_search(data, target):
  	# 남은 데이터 길이가 1 이상일 경우
    if len(data) > 1:
        medium = int(len(data)/2)
        left_list = data[:medium]
        right_list = data[medium:]
        if data[medium] == target:
            return True
        elif data[medium] < target:
            return binary_search(right_list, target)
        else:
            return binary_search(left_list, target)
        return False
   	# 남은 데이터 길이가 1일 경우
    elif len(data) == 1:
        if data[0] == target:
            return True
        else:
            return False
   	# 남은 데이터 길이가 0일 경우
   else:
    		return False
print(binary_search(data_list, 10))
```

`강의 모범 답안 코드`

```python
import random
data_list = random.sample(range(15), 10)
data_list = sorted(data_list)

def binary_search(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search < data[medium]:
            return binary_search(data[:medium], search)
        else:
            return binary_search(data[medium:], search)

print(binary_search(data_list, 1))

```

## 4. 알고리즘 분석

한 번 처리할 때마다 분석할 대상이 반으로 감소함.
n개의 리스트를 매번 2로 나누어, 1이 될 때까지 k번의 비교연산을 진행.

k = log2n 이고, 마지막 1이 되었을 때도 비교연산을 한번 수행하기에 O(log2n +1) 이지만 빅오 표기법으로는 **O(log2n)** = O(logn) 이다.

## 5. Lesson learned

파이썬의 내장 정렬 메서드 종류:  `sorted(list)` , `list.sort()`

두 함수의 차이는 새로운 리스트를 리턴하냐, 아니면 원래  리스트를 변경하고 None을 반환냐의 차이.

#### sorted(list) - 모든 iterable 객체(리스트, 튜플, 딕셔너리 등) 에 대해 새로운 정렬된 리스트를 반환함

```python
sorted([5, 2, 3, 1, 4]) # 새롭게 정렬된 리스트인 [1,2,3,4,5] 리턴
```

#### list.sort - 오직 리스트에만 적용 가능하며 원본 리스트를 수정하고 None을 반환함

```python
a = [5, 2, 3, 1, 4]
a.sort() # None 리턴
print(a) # 원본 리스트가 [1, 2, 3, 4, 5] 로 변경됨
```