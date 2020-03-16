# 다익스트라 알고리즘 (Dijsktra algorithm)

다익스트라 알고리즘은 최단 경로 문제를 푸는 알고리즘의 한 종류이다.

## 1. 최단 경로 문제란?

- 최단 경로 문제란 **두 노드를 잇는 가장 짧은 경로**를 찾는 문제임
- 가중치 그래프에서 **간선의 가중치 합이 최소**가 되도록 하는 경로를 찾는 것이 목적

## 2. 최단 경로 문제의 종류

1. 단일 출발 및 단일 도착 최단 경로 문제
   그래프 내의 특정 노드 u 에서 출발해, 또 다른 특정 노드 v 에 도착하는 가장 짧은 경로를 찾는 문제
2. 단일 출발 최단 경로 문제 ⭐️ 다익스트라 알고리즘이 이 문제에 해당!
   그래프 내의 특정 노드 u 와 그래프 내 다른 모드 노드 각각의 가장 짧은 경로를 찾는 문제
3. 전체 쌍 최단 경로 문제
   그래프 내의 모든 노드 쌍 (u,v) 에 대한 최단 경로를 찾는 문제

## 3. 다익스트라 알고리즘

### 3-1. 다익스트라 알고리즘이란?

다익스트라 알고리즘은 하나의 정점에서, 다른 모든 정점 간의 각각의 최단 경로를 구하는 알고리즘.

- 첫 정점을 기준으로 연결되어 있는 정점들을 추가해가며 **최단 거리를 갱신**하는 기법
- BFS와 유사
- 다익스트라 알고리즘은 다양한 변형 로직이 있으나, 가장 개선된 **우선순위 큐**를 사용하는 방식에 집중할 것

### 3-2. 우선순위 큐를 활용한 다익스트라 알고리즘

우선순위 큐는 MinHeap 방식을 활용해서 현재 **가장 짧은 거리**를 가진 노드 정보를 먼저 꺼냄.

1) **첫 정점을 기준으로 배열을 선언**하여 첫 정점에서 각 정점까지의 거리를 저장

- **초기에 첫 정점의 거리는 0, 나머지는 무한대 (inf) 로 저장**함
- **우선순위 큐에 (첫 정점, 거리 0) 만 넣음**

2) 우선순위 큐에서 노드를 꺼냄

- 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
- 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교함
- 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트함
- 배열과 해당 노드의 거리가 업데이트 된 경우, 우선순위 큐에 넣음
  - 결과적으로 BFS 방식과 유사하게 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
  - 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 루트를 가진 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음.

3) 2번을 우선순위 큐에 꺼낼 노드가 없을 때 까지 반복한다

결과적으로 배열은 출발점과 각 노드들까지의 최단 거리를 가지게 된다.

### 3-3. 다익스트라 알고리즘 파이썬 구현

#### 1) heapq 라이브러리 활용을 통해 우선순위 큐 사용하기

데이터가 리스트 형태일 경우, **0번 인덱스를 우선순위로 인지**해 우선순위가 낮은 순서대로 pop 할 수 있음.

```python
import heapq
queue = []
heapq.heappush(queue, [2,'A']) # heapq에 데이터 넣는 메소드: heappush
heapq.heappush(queue, [5,'B'])
heapq.heappush(queue, [1,'C'])
for index in range(len(queue)):
  print(heapq.heappop()) # heapq에서 데이터 빼는 메소드: heappop
```

heapq 라이브러리의 `heappush` , `heappop` 메소드를 사용하면 최소 heap의 구조를 가지고 있는 우선순위 큐를 만들 수 있다.

#### 2) 그래프 표현하기

![img](https://www.fun-coding.org/00_Images/dijkstra.png)

[복습] 파이썬에서 그래프는 딕셔너리 형태로 표현한다!

```python
mygraph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}
```

```python
# 그래프와 시작 노드 정보를 받음
def dijsktra(graph, start):
    # 초기화 - 출발점과 각 노드 간의 최단 거리를 저장한 배열(딕셔너리 자료형) 만들기
    distances = {node: float('inf') for node in graph}
    distance[start] = 0
    queue = []
    
    # 순서 중요! queue에 들어오는 리스트 형태의 데이터의 0번 인덱스를 우선순으로 인지한다. 따라서 [딕셔너리의 value 값, 딕셔너리의 key 값] 형태의 리스트로 우선순위 큐에 넣어주어야 한다.
    # 즉 데이터가 [distance, node] 형태로 되어 있는 것
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        # 이미 배열에 있는 최단거리가 지금 찾은 거리보다 짧다면 그냥 이후의 과정을 skip 해주면 된다
        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                # 배열을 업데이트 해주고
                distances[adjacent] = distance
                # [지금 찾은 최단거리, 노드] 를 우선순위큐에 넣어준다
                heapq.heappush(queue, [distance, adjacent])

    return distances
  
print(dijsktra(mygraph, 'A'))
```

### 3-4. 다익스트라 알고리즘 시간복잡도 분석

다익스트라 알고리즘은 크게 다음 두가지 과정을 거침

1) 각 노드마다 인접한 간선들을 모두 검사하는 과정
2) 우선순위 큐에 노드/거리 정보를 넣고 삭제(pop) 하는 과정

과정1: 각 노드는 최대 한번씩 방문하므로 그래프의 모든 간선은 최대 한 번씩 검사. 즉, 노드마다 인접한 간선들을 모두 검사하는 과정은 O(E)
과정 2: 우선순의 큐에 가장 많은 노드, 거리 정보가 들어가는 경우! 우선순위 큐에 추가하는 행위는 간선마다 최대 한 번 일어날 수 있으므로 최대 O(E), O(E)개의 노드/거리 정보에 대해 우선순위 큐 minheap 구조를 유지하는 작업은 O(logE) 가 걸림. 따라서 해당 과정의 시간 복잡도는 O(ElogE)

결과적으로 O(E) + O(ElogE) = O(ElogE)

### 3-5. [참고] 최단 경로 출력하기

```python
def dijsktra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대로 초기화
    distances = {vertex: [float("inf"), start] for vertex in graph}
    distances[start] = [0, start]
    # 모든 정점이 저장될 큐(최소힙) 생성
    queue = []
    # 그래프의 시작 정점과 시작 정점의 거리를 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[adjacent][0]:
                # 기존 알고리즘과의 차이점이라면, current_vertex 도 저장한다는 점! 어딜 거쳐서 가는게 최단인지!
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])
    path = end
    path_output = end + '->'
    # 최초 정점 직전까지 계속해서 반복문을 돌며 최단경로의 경유 노드를 찾아나감
    while distance[path][1] != start:
        path_output += distances[path][1] + '->'
        # 최단 경로를 위한 직전 경유지를 다시 path에 할당
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances
  
dijsktra(mygraph, "A", "F")
```

