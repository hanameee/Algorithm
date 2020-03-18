# 프림 알고리즘 (Prim's algorithm)

## 1. 프림 알고리즘이란?

크루스칼 알고리즘과 마찬가지로 최소 신장 트리 (MST) 를 구하기 위한 알고리즘으로, 역시 **탐욕 알고리즘**을 기초로 한다.

## 2. 프림 알고리즘 vs 크루스칼 알고리즘

[공통점]

- 둘다 탐욕 알고리즘을 기초로 하고 있음.

[차이점]

- 크루스칼 알고리즘은 **전체 간선들 중 가장 가중치가 작은 간선부터 사이클이 생기지 않게 선택**하면서 MST를 구함.
- 프림 알고리즘은 **특정 정점에서 시작해, 해당 정점에 연결된 간선들 중 가장 가중치가 작은 간선을 선택**해가며 MST를 구함.

## 3. 프림 알고리즘 동작 방식 이해

1. 임의의 정점을 선택, **'연결된 노드 집합'**에 삽입
2. 선택된 정점에 연결된 간선들을 간선 리스트에 삽입
3. 간선 리스트에서 최소 가중치를 가지는 간선부터 추출해서,
   - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 이미 들어 있다면, 스킵함 (cycle 방지)
   - 해당 간선에 연결된 인접 정점이 '연결된 노드 집합'에 들어 있지 않으면, 해당 간선을 선택하고, 해당 간선 정보를 **'최소 신장 트리'**에 삽입
4. 추출한 간선은 간선 리스트에서 제거 (pop)
5. **간선 리스트에 더 이상의 간선이 없을 때까지** 3-4번을 반복

## 4. 프림 알고리즘 코드 작성

```python
# 중복된 간선은 빼고 표현, 노드는 별도로 표현할 필요 X
from collections import defaultdict
from heapq import *

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node, edges):
    adjacent_edges = defaultdict(list)
    mst = list()
    for weight, n1, n2 in edges:
        # 이 과정에서 자동으로 간선들이 양쪽 노드에 중복으로 잘 들어감
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    connected_nodes = set(start_node)  # 연결된 노드들을 집합 형태로
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)  # n1은 원래 정점, n2가 인접 정점
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst


print(prim('A', myedges))
```

## 5. 시간 복잡도

최악의 경우, while 구문에서 모든 간선에 대해 반복하고 O(E), 한 loop 당 push 하며 최소 힙 구조를 유지하는 데에 O(logE) 만큼의 시간이 걸리므로 (heap에 모든 간선이 다 들어갈 최악의 경우) 결과적으로 O(ElogE) 시간 복잡도를 가짐

그런데 일반적으로 프림 알고리즘의 시간복잡도는 **O(ElogV)** 로 나타내는 경우가 많음! 그 이유는 아래 개선된 프림 알고리즘에서!

## 6. 참고 - 개선된 프림 알고리즘

기존 프림 알고리즘이 **간선**을 중심으로 candidate_edge_list 라는 우선순위 큐를 적용했다면, 개선된 프림 알고리즘은 **노드** 를 중심으로 우선순위 큐를 적용한다.

어떻게 노드를 중심으로 하는가?
노드마다 **key 값**을 매겨서 인접 간선 후보들의 weight 중 가장 작은 값으로 key 값을 업데이트 한다.
가장 작은 key값을 가진 노드부터 pop을 하고, 이때 가장 작은 key 값으로 선택되었던 인접 간선 후보를 MST에 추가한다.

1) 초기화 - 노드:key 구조를 만들어놓고, 특정 정점의 key값은 0, 이외의 정점들의 key값은 무한대로 놓음. 모든 정점:key 값은 우선순위 큐에 push

2) 가장 key값이 작은 노드:key를 pop 한 후, (pop 하므로 해당 정점:key 정보는 우선순위 큐에서 삭제됨), ( = extract min 로직) 해당 노드의 인접 노드들에 대해 key 값과 연결된 가중치 값을 비교하여 key값이 작으면 해당 인접노드:key 값을 갱신

3) 노드:key 값 갱신시, 우선순위 큐는 **최소 key값을 가지는 노드:key 를** 루트 노드로 올려놓도록 재구성함 (decrease key 로직이라고 부름) > 우리는 push 한 녀석들을 pop 할 때 최소값을 빼는 것만 배웠지, 이미 들어가 있는 애들의 값을 변경했을 때도 힙 구조를 유지하게끔 하는 것은 배운 적이 없다.😨

따라서 우선순위 큐 (최소힙) 에서, **이미 들어가 있는 데이터의 값 변경** 시, 최소값을 가지는 데이터를 루트 노드로 올려놓도록 재구성하는 기능 > heapdict 라이브러리를 통해 해당 기능을 간단히 구현할 것!

### 개선된 프림 알고리즘 코드 구현

```python
from heapdict import heapdict

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}


def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key
        for adjacent, weight in mygraph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node
    return mst, total_weight

```

### 개선된 프림 알고리즘 시간복잡도

1) 초기화 하는 부분: 노드 갯수 만큼 반복하므로 O(V)

2) keys 에서 pop 하며 MST를 업데이트 하는 부분 : while 구문은 노드의 갯수 만큼 실행되므로 O(V), 그 루프 안에서 popitem 한 후 힙을 재구성하는 부분은 O(logV) 이기에 전체적으로는 O(VlogV)

3) key 값을 업데이트 하는 부분 : 루프 한번 당 해당 노드에 연결된 인접간선 만큼 도는데, 전체적으로 보면 while과는 별개로 그냥 O(E) 임. 그런데 노드의 key 값을 계속해서 업데이트하면 그 때마다 keys 의 힙 구조를 재구성해야함. 최악의 경우, 힙 구조 안에 들어가 있을 수 있는 데이터의 갯수는 최대 노드 갯수만큼이니 O(logV) 이고, 매 간선 마다 업데이트가 된다면 **O(ElogV)**

전체적으로는 O(V) + O(VlogV) + O(ElogV) 인데, 일반적으로 E>V 이므로 (최대 V^2 = E) 시간복잡도는 O(ElogV) 임.

## 7. Lesson Learned

### heapq 라이브러리 활용을 통해 우선순위 큐 사용하기

기존에 사용했던 `heapq.heappush`, `heapq.heappop`

```python
import heapq
queue = []
graph_data = [[2,'A'], [5,'B'], [3,'C']]

# 데이터를 아무렇게나 큐에 집어넣어도
for edge in graph_data:
  heapq.heappush(queue,edge)

# heappop 메소드를 사용하여 pop하면 항상 최소값이 pop됨
for index in range(len(queue)):
  print(heapq.heappop(queue))
```

`heapq.heapify` 함수를 통해 리스트 데이터를 heap 형태로 한번에 변환

```python
import heapq
graph_data = [[2,'A'], [5,'B'], [3,'C']]
# 별도의 큐가 필요 없음

heapq.heapify(graph_data)
for index in range(len(graph_data)):
  print(heapq.heappop(graph_data))
```

### collections 라이브러리의 defaultdict 함수 사용하기

```python
from collections import defaultdict

list_dict = defaultdict(list)
list_dict['key1'] # []
```

별도로 key에 대한 value를 지정하지 않아도 (초기화하지 않아도), 빈 리스트로 초기화를 해준다.

원래는 딕셔너리에 초기화 되지 않은 key 값을 호출하면 KeyError 이 발생하나, defaultdict 를 사용하면 key 값을 초기화하지 않아도 어떤 key에 대해서도 미리 지정해둔 기본값을 value로 받을 수 있다.

```python
from collections import defaultdict

# 어떤 값을 defaultdict의 파라미터로 넘기느냐에 따라 기본값이 달라짐
list_dict = defaultdict(int)
list_dict['key1'] # 0

list_dict = defaultdict(str)
list_dict['key1'] # " "
```

