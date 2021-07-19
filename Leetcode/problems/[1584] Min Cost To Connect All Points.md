# [1584] Min Cost To Connect All Points

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | Easy **Medium** Hard             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | 약 2시간                         |
| 시간복잡도  | O(V+E)                           |

## Result

![1584](1584.png)

## Solving

최소신장 트리(MST)의 개념을 아예 까먹고 있었다 :) 한시간 정도 고민하다가 모르겠어서 discussion 보고, MST 문제인걸 파악하고 크루스칼 알고리즘이랑, 프림 알고리즘 복습해서 다시 풀었다.

크루스칼으로 일단 한번 풀어봤는데 시간복잡도가 살벌하게 나왔다... 다른 풀이도 봐야 할 듯.

## Source

```python
class Solution(object):
    parent = [None for _ in range(1000)]
    rank = [None for _ in range(1000)]

    def makeSet(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, X, Y):
        root1 = self.find(X)
        root2 = self.find(Y)

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1

    def getManhattanDistance(self, X, Y):
        return abs(X[0]-Y[0]) + abs(X[1]-Y[1])

    def minCostConnectPoints(self, points):
        edges = []
        answer = 0
        for i in range(len(points)):
            self.makeSet(i)
            for j in range(i+1, len(points)):
                edges.append(
                    [self.getManhattanDistance(points[i], points[j]), i, j])
        edges.sort(key=lambda x: x[0])
        for e in edges:
            dist, X, Y = e
            if self.find(X) != self.find(Y):
                self.union(X, Y)
                answer += dist
        return answer
```

