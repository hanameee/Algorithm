# 깊이 우선 탐색 (Breadth-First Search)

## 1. BFS 와 DFS 란?

대표적인 그래프 **탐색** 알고리즘

- 너비 우선 탐색 (Breadth First Search): 정점들과 같은 레벨에 있는 노드들 (**형제 노드**) 을 먼저 탐색하는 방식
  - 한 단계씩 내려가면서, 해당 노드의 형제 노드들을 먼저 순회
- 깊이 우선 탐색 (Depth First Search): 정점의 **자식 노드**들을 먼저 탐색하는 방식
  - 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순회

## 2. DFS 알고리즘 구현

DFS 알고리즘은 **스택과 큐 자료구조**를 활용함. (복습: BFS는 큐 2개를 사용)
`need_visit` 은 스택을, `visited` 는 큐를 사용함

```python
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# dfs 로직
def dfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        # 맨 마지막 index를 pop 한다
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return(visited)


print(dfs(graph, "A"))
```

## 3. 시간 복잡도

일반적인 DFS 시간 복잡도

- 노드 수: V
- 간선 수: E

DFS 코드에서 while need_visit 은 V+E 번 만큼 수행함 = 시간복잡도 **O(V+E)**

## 4. Lesson Learned

https://docs.python.org/ko/3/tutorial/datastructures.html 에서 리스트 메서드 복습

