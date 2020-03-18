# 크루스칼 알고리즘 (Kruskal's algorithm)

## 1. 크루스칼 알고리즘이란?

최소 신장 트리 (MST) 를 구하기 위한 알고리즘으로, **탐욕 알고리즘**을 기초로 한다.

1. 모든 정점을 **독립적인 집합**으로 만든다.
2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 **비교**한다.
3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다. (최소 신장 트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임) - 이 **사이클이 안생기도록 하기 위한 로직**이 중요함 ⭐️

## 2. Union-Find 알고리즘이란?

- Disjoint Set을 표현할 때 사용하는 알고리즘으로 트리 구조를 활용하는 알고리즘
- 간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 (합칠 때) 사용
- Disjoint Set이란?
  - **서로 중복되지 않는 부분 집합**들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조 (서로소 집합 자료구조)

Union-Find 알고리즘에서는 부분집합을 **트리**로 관리함.

(1) **Union 연산** : 두 부분 집합을 하나의 집합으로 합치는 연산 = 두개의 트리를 하나의 트리로 만드는 것
(2) **Find 연산** : 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프 (부분집합) 에 속하는지 판별하기 위해 각 그룹의 최상단 원소 (즉, 루트 노드)를 확인하는 연산 = 크루스칼 알고리즘에서는 연결했을 때 싸이클이 생기는지 안생기는지 확인하기 위해 사용됨.

## 3. 최적화된 Union-Find 알고리즘

- Union 순서에 따라서, 최악의 경우 링크드 리스트와 같은 형태가 될 수 있음.
- 이 때는 Find/Union 시 계산량이 O(N) 이 될 수 있으므로, 해당 문제를 해결하기 위해, union-by-rank, path compression 기법을 사용함

### union by rank

![img](https://www.fun-coding.org/00_Images/unionbyrank_findunion.png)

- 각 트리에 대해 높이(rank)를 기억해 두고,
  - Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임 (항상 높이가 큰 트리가 루트 노드가 되게끔)
  - 높이가 같은 두 개의 트리를 합칠 때는 한 쪽의 트리 높이를 1 증가시켜주고, 다른 쪽의 트리를 해당 트리에 붙임

왜 이렇게 할까?

초기화 시 모든 원소는 rank 0인 개별 집합임. 높이가 h인 트리가 만들어지려면, 높이가 h-1 인 두개의 트리가 합쳐져야 함. 높이가 h-1인 트리를 만들기 위해 최소 n개의 원소가 필요하다면, 높이가 h인 트리가 만들거지기 위해서는 최소 2n개의 원소가 필요함.

따라서 union-by-rank 기법을 사용하면 union/find 연산의 시간복잡도는 O(logN) 으로 낮출 수 있음.

### path compression

![img](https://www.fun-coding.org/00_Images/pathcompression_findunion.png)

- Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
- Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음

Union by rank 와 path compression 기법 사용 시, 시간 복잡도는 O(Mlog*N). n이 무한정 커지더라도 거의 상수에 근접함.

## 4. 크루스칼 알고리즘 코드 작성

1) 그래프 코드 작성 - 딕셔너리 자료구조 이용

```python
graph = {
  # 노드
  'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
  # 간선 (가중치, 시작점, 끝나는점)
  'edges':  [
    (7,'A','B'),
    (5,'A','D'),
    (7, 'B', 'A'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (8, 'C', 'B'),
    (5, 'C', 'E'),
    (5, 'D', 'A'),
    (9, 'D', 'B'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (7, 'E', 'B'),
    (5, 'E', 'C'),
    (7, 'E', 'D'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (6, 'F', 'D'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (11, 'G', 'F')
  ]
}
```

2) 알고리즘 작성

```python
parent = dict()
rank = dict()


# 각각의 노드들을 독립적인 부분집합으로 초기화
def make_set(node):
    parent[node] = node  # 자기 자신
    rank[node] = 0


# 파라미터로 받은 노드가 속한 부분집합의 root 노드를 리턴한다
def find(node):
    # path compression
    if parent[node] != node:
        # 재귀적으로 root 노드를 찾아나가고, root 노드를 현재 노드의 직속부모로 만들어줌 = path compression
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:  # root1의 높이가 root2의 높이보다 크다면,
        parent[root2] = root1  # 더 작은 쪽 (root2) 를 root1의 자식으로 연결
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph):
    mst = list()  # 간선의 리스트
    # 1. 초기화 각 노드별로 부분집합을 만든다
    for node in graph['vertices']:
        make_set(node)
    # 2. 간선 가중치 기준 오름차순으로 sorting
    edges = graph['edges']
    edges.sort()
    # 3. 사이클 없다면 간선 연결
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst


print(kruskal(mygraph))
```

## 5. 크루스칼 알고리즘 시간 복잡도

크루스칼 알고리즘의 시간 복잡도는 O(E log E)

1) 초기화 과정 : 노드의 갯수 만큼 loop를 한번 도니까 O(V)
2) 간선 정렬 과정 : 퀵소트 사용한다면 간선 갯수를 E라고 할 때 O(E log E)
3) union-find 과정 : 간선들을 하나씩 돌며 union-find (O(1)) 만큼의 작업을 진행하므로 O(E)

세 작업 중 가장 시간복잡도가 높은 과정은 간선 정렬 과정. 크루스칼 알고리즘은 따라서 O(E log E) 만큼의 시간복잡도를 가진다.

