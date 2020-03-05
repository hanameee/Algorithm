# 큐

### 파이썬 queue 라이브러리

- **queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공**

- 프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조를 사용

  - Queue(): 가장 일반적인 큐 자료 구조

  - LifoQueue(): 나중에 입력된 데이터가 먼저 출력되는 구조 (= 스택 구조)

  - PriorityQueue(): 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

리스트로 queue 구현하기

```python
queue_list = list()

def enqueue(data):
    queue_list.append(data)
    
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data
  
for index in range(1,11):
    enqueue(index)
    print("큐에 %d를 넣어따" % index)

dequeue()
dequeue()
print(len(queue_list)) # 8

```

# 