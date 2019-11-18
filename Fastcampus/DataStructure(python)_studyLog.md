# 배열 (Array)

* 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조

## c++ 과 python의 배열 비교

`c++`

```c++
#include <stdio.h>

int main(int argc, char * argv[])
{
    char country[3] = "US";
    printf ("%c%c\n", country[0], country[1]);
    printf ("%s\n", country);    
    return 0;
}
```

`python`

```python
country = 'US'
print (country)
```

## Python 의 배열

- 파이썬에서는 **리스트 타입**이 배열 기능을 제공

```python
# 1차원 배열: 리스트로 구현시
data_list = [1, 2, 3, 4, 5]
data_list
```

```python
# 2차원 배열: 리스트로 구현시
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_list
```

- 배열에서 특정 알파벳의 등장 횟수 세기

```python
dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James']

count = 0;
for data in dataset:
  for index in range(len(data)):
    if data[index] == 'a':
      count += 1
print(count)
```



# 큐 (Queue)

- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조 (줄을 서는 행위와 유사)
- FIFO (선입선출)

## 1. Queue의 기능

1) enqueue : 큐에 데이터를 넣는 기능
2) dequeue : 큐에서 데이터를 꺼내는 기능

## 2. 파이썬 queue 라이브러리

일반적인 (FIFO) 큐 외에 다양한 정책이 적용된 큐들이 있음.

- Queue() : 가장 일반적인 큐 자료 구조
- LifoQueue() : 스택 구조 (나중에 입력된 데이터가 먼저 출력)
- PriorityQueue() : 데이터마다 우선순위를 넣어, 우선순위 높은 순으로 데이터 출력

queue 라이브러리를 사용해 각각의 큐를 구현해보자.

### 2.1) 라이브러리를 사용한 일반적인 Queue 만들기

`Queue 생성`

```python
import queue
data_queue = queue.Queue() # 라이브러리명.클래스명
```
`데이터 추가하기`

```python
data_queue.put('data1') # enqueue 명령어 = put 
data_queue.put(1) # 숫자도 추가 가능
```

`큐 길이`

```python
data_queue.qsize() # length 확인 - 현재 상태에서는 2
```

`데이터 꺼내기`

```python
data_queue.get() # FIFO 정책이 자동으로 적용되었으므로 get에 별다른 파라미터 필요 X
data_queue.qsize() # 현재 상태에서는 1
```

### 2.2) 라이브러리를 사용한 LifoQueue 만들기

`LifoQueue 생성`

```python
import queue
data.queue = queue.LifoQueue()
```

나머지 추가/길이/꺼내기 명령어는 동일

### 2.3) 라이브러리를 사용한 PriorityQueue 만들기

`우선순위 큐 (PriorityQueue) 생성`

```python
import queue
data_queue = queue.PriorityQueue()
```

`데이터 추가하기`

```python
# get의 파라미터로 (우선순위,데이터) 튜플을 넘겨준다
data_queue.put((10, "korea")) # 데이터는 "korea", 우선순위는 10
data_queue.put((5,1)) # 데이터는 1, 우선순위는 5
data_queue.put((15, "hannah")) # 데이터는 "hannah", 우선순위는 15
```

**priority 번호가 낮을수록 우선순위가 높은 것!**

data_queue.get을 하면 5 - "korea" - "hannah" 순으로 데이터가 출력된다



+) 실제로 어디에 큐가 많이 쓰이나?

운영체제에서 멀티태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용된다.



## 리스트로 queue 구현해보기

```python
queue_list = list() # 리스트 변수 만들기

def enqueue(data):
  queue_list.append(data)

def dequeue():
  data = queue_list[0]
  del queue_list[0]
  return data
```

### 사용해보기

```python
for index in range(10):
  enqueue(index)

len(queue_list)

dequeue()
```

