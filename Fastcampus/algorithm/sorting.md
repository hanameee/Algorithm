# 정렬

정렬 (sorting): 어떤 데이터들이 주어졌을 때 이를 정해진 순서대로 나열하는 것

## 1. 버블 정렬 (bubble sort)

버블정렬이란?
두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘.

`내가 처음 작성한 버블정렬`

```python
def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j+1] < data[j]:
                data[j], data[j+1] = data[j+1], data[j]
```

위 알고리즘은 항상 O(n^2) 임. 완전 정렬이 되어 있을 경우 swap이 한번도 되지 않음을 이용해 swap 횟수가 0일시 즉시 loop를 탈출하게 할 수 있다.

`개선된 버블정렬`

```python
def bubble_sort(data):
    for i in range(len(data)-1):
        swap = False
        for j in range(len(data)-1-i):
            if data[j+1] < data[j]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
        if not swap:
            break
```

`테스트해보기`

```python
import random
data = random.sample(range(100), 50)
print(data)
bubble_sort(data)
print(data)
```

### 알고리즘 성능

반복문이 2개이므로 O(n^2) : 최악의 경우 n(n-1)/2 번 돈다
최선의 경우 O(n) : 처음 한번만 돌고 break



## 2. 선택 정렬 (selection sort)

## 3. 삽입 정렬 (insertion sort)