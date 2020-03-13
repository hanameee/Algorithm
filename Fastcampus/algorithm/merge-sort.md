# 병합 정렬 (merge sort )

## 1. 병합 정렬이란?

- 재귀용법을 활용한 정렬 알고리즘
  1. 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
  2. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
  3. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.

 ## 2. 코드로 이해하기

```python
import random
data_list = random.sample(range(100), 9)
print(data_list)


def merge(left, right):
    result = list()
    left_index = 0
    right_index = 0
    # case1: left/right 아직 남아있을 경우
    # index 값이 len(list) 와 같아지면 loop를 탈출해야함 - 마지막 원소까지 다 비교한 것이기 때문에
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    # 위 loop를 탈출하는 시점은 left가 끝났거나 right가 끝났거나 둘 중 하나
    # case2: left 만 남아있을 경우
    while len(left) > left_index:
        result.extend(left[left_index:])
        break
    # case3: right 만 남아있을 경우
    while len(right) > right_index:
        result.extend(right[right_index:])
        break
    return result


def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data)/2)
    # 여기서 계속 재귀적으로 분리를 하고
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    # 재귀적으로 계속 merge를 함
    return merge(left, right)


print(mergesplit(data_list)) 
```

## 3. 알고리즘 분석

![img](https://www.fun-coding.org/00_Images/mergesortcomplexity.png)

- 원래 데이터의 양을 n이라고 했을 때, depth i의 노드 하나 당 데이터 양은 n/2^i
- depth n의 전체 노드 갯수는 2^i
- 한 depth 의 계산량은 노드 하나 당 데이터 양 * 전체 노드 갯수 = n
- 따라서 각 단계에서 계산하는 양은 항상 O(n)
- 단계는 log2n 개 만큼 만들어짐
- 따라서 전체 시간 복잡도는 **O(n * logn)**

## 4. lesson learned

Python 에서 append 와 extend 의 차이

`append`

```python
# object를 맨 뒤에 추가함
x = [1, 2, 3]
x.append([4, 5])
print (x)
```

`extend`

```python
# extend()는 iterable 객체 (리스트, 튜플, 딕셔너리 등) 의 엘레멘트를 list에 append함
x = [1, 2, 3]
x.extend([4, 5])
print (x)
```

