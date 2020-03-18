# 최소 신장 트리의 이해 (Minimum Spanning Tree)

## 1. 신장 트리란?

- 모든 노드가 연결되어 있으면서, 트리(비순환 그래프)의 속성을 만족하는 그래프

## 2. 신장 트리의 조건

- 본래 그래프의 **모든 노드를 포함**해야 함
- 모든 노드가 서로 연결
- 트리의 속성을 만족시킴 (비순환 = 사이클이 존재하지 않음)

## ![img](https://www.fun-coding.org/00_Images/spanningtree.png)

## 3. 최소 신장 트리 (MST)

- 가능한 Spanning Tree 중에서, 간선들의 가중치의 합이 최소인 Spanning Tree를 지칭함.

![img](https://www.fun-coding.org/00_Images/mst.png)

## 4. 최소 신장 트리 알고리즘

그래프에서 MST 를 찾을 수 있는 알고리즘들이 존재함.
그 대표적인 MST 알고리즘이 (1) Kruskal's algorithm, (2) Prim's algorithm.

