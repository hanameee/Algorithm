# 퀵 정렬 (quick sort )

## 1. 퀵 정렬이란?

- 정렬 알고리즘의 꽃🌸
- **기준점(pivot)**을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right) 으로 모으는 함수를 작성
- 각 왼쪽(left), 오른쪽(right) 부분은 **재귀용법**을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복
- 함수는 왼쪽(left) + 기준점(pivot) + 오른쪽(right) 을 리턴함

## 2. 코드로 이해하기

```python
def quicksort(data):
  	# data의 length 가 0 일 수도 있다!
    if len(data) <= 1:
      	# 리스트의 형태로 리턴해야 함
        return data
    pivot = data[0]
    left = list()
    right = list()
    for index in range(1, len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])
    return quicksort(left)+[pivot]+quicksort(right)
```

### list comprehension 을 통해 조금 더 간결하게 작성하기

```python
def quicksort_s(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    
    # list comprehension 에 if 문까지 활용하여 아래와 같이 더욱 간결하게 작성 가능
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if pivot <= item]
    return quicksort_s(left) + [pivot] + quicksort_s(right)
```

## 3. 알고리즘 분석

일반적인 경우, quick sort의 시간 복잡도는 O(n log n)
최악의 경우 (pivot이 모든 경우에 최댓값/최솟값 일 경우) 모든 데이터를 비교해야 해서 O(n^2)

가장 평균적인 형태는 pivot 을 기준으로 하여 left, right가 반반 있는 상태임.
이 때는 depth 가 log n 만큼 생성이 되고 ( = 이진트리와 유사) 각 depth 에서 pivot과 비교해 정렬을 하기 위해 n 의 시간이 걸린다.
따라서 시간 복잡도는 n * log n = O(n log n) 



