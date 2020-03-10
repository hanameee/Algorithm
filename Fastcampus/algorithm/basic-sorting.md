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
        if swap == False:
            break
    return data
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
최선의 경우 O(n) : 완전 정렬이 되어 있는 경우 처음 한번만 돌고 break

### lesson learned

- swap을 boolean으로 표시하는 방법
  default를 False로 두고, 한 번이라도 해당 로직을 탔다면 True가 되게끔. 따라서 Loop가 끝난 이후에도 여전히 False라는 건 한번도 해당 로직을 타지 않았다는 사실을 나타낸다는 것.
- return 문 위치 조심...!



## 2. 선택 정렬 (selection sort)

선택정렬이란?
다음과 같은 순서를 반복하며 정렬하는 알고리즘

1. 주어진 데이터 중, 최소값을 찾음
2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

`내가 처음 작성한 선택정렬` 

```python
def selection_sort(data):
    for i in range(len(data)-1):
        min_index = i+1 # 잘못 이해했던 부분
        for j in range(i+1, len(data)-1):
            if data[min_index] > data[j+1]:
                min_index = j+1
        if data[i] > data[min_index]: # 이 과정은 필요가 없다. 이미 검증됨
            data[i], data[min_index] = data[min_index], data[i]
```

`모범답안 선택정렬`

```python
def selection_sort(data):
    for i in range(len(data)-1):
      	# 정렬되지 않은 부분 중 가장 작은 index를 최소인덱스로 둔 것이고
        min_index = i
        for j in range(i+1, len(data)):
          	# 해당 index의 값과 j를 비교하면서 최소인덱스를 update
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
```

### 알고리즘 성능

반복문이 2개이므로 O(n^2) : 최악의 경우 n(n-1)/2 번 돈다


## 3. 삽입 정렬 (insertion sort)

삽입정렬이란?

- 삽입 정렬은 두 번째 인덱스부터 시작 (첫 번째 인덱스는 정렬되어 있다고 가정)
- 해당 인덱스(key 값) 바로 앞에 있는 데이터(B)부터 비교해서 key 값이 더 작으면, B값을 뒤 인덱스로 복사
- 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동 (큰 데이터를 일단 한번 만나면 그 이후는 고려 X)

`내가 처음 작성한 삽입정렬 `

```python
def insertion_sort(data):
    for i in range(len(data)-1):
      	# 나는 현재 바라보고 있는 data를 변수에 저장해두고 비교하는 식으로 구현
        sorting_data = data[i+1]
        for j in range(i+1):
            if sorting_data < data[i-j]:
                data[i-j+1] = data[i-j]
                if i-j == 0:
                    data[0] = sorting_data
            else:
                data[i-j+1] = sorting_data
                break
```

`모범답안 삽입정렬`

```python
def insertion_sort(data):
    for i in range(len(data)-1):
      	# 모범 답안은 key 값을 줄이며 swap 해가는 식으로 구현
        for j in range(i+1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data
```

### 알고리즘 성능

반복문이 2개이므로 O(n^2) : 최악의 경우 n(n-1)/2 번 돈다
최선의 경우 O(n) : 완전 정렬이 되어 있는 경우 처음 한번만 돌고 break

### lesson learned

- For 문에서 range를 활용해 index 뒤부터 가져오는 방법

  ```python
  for j in range(i+1, 0, -1):
    if data[j] < data[j-1]:
      data[j], data[j-1] = data[j-1], data[j]
  ```

  

