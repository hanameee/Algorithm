# [307] Range Sum Query - Mutable

## Info

### 결과값

| 항목        | 평가                             |
| ----------- | -------------------------------- |
| 통과        | **AC** WA                        |
| 문제 난이도 | Easy **Medium** Hard             |
| 체감 난이도 | Easy **Medium** Hard             |
| 언어        | C C++ Java **Python** Javascript |
| 해결 시간   | -                                |
| 시간복잡도  | O(N)                             |

## Result

-

## Solving

rangeSum은 누적합으로 하면 되겠다 싶었는데, update를 대체 어떻게 해야 할지 모르겠어서 못풀었다🥲

## Solution

찾아보니 **Segment Tree, Binary Indexed Tree**를 사용하는 문제라고...! Segment Tree는 공부해본 기억이 없다...

### Segment Tree

데이터의 구간 합을 가장 빠르고 간단하게 구할 수 있는 자료구조인 Segment Tree는 RangeSum, update 연산을 모두 O(Logn)에 수행한다.

아래는 Solution 보고 공부한 코드.

## Source

```python
def getMid(start, end):
    return (start+end) // 2

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray(object):

    def __init__(self, nums):
        def createTree(nums, l, r):
            # base case
            if l > r:
                return None
            # leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = getMid(l, r)
            root = Node(l, r)
            # 재귀적으로 Segment Tree 생성
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total
            return root

        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, index, val):
        def updateVal(root, index, val):
            # leaf 노드인 경우
            if root.start == root.end:
                root.total = val
                return val
            # leaf 노드가 아니라면
            mid = getMid(root.start, root.end)
            # mid보다 작으면 left subtree에 있을 것
            if index <= mid:
                updateVal(root.left, index, val)
            # mid보다 크면 right subtree에 있을 것
            else:
                updateVal(root.right, index, val)
            # recursive call이 끝나고 나면 변경된 값을 부모에 반영
            root.total = root.left.total + root.right.total
            return root.total
        return updateVal(self.root, index, val)

    def sumRange(self, l, r):
        def rangeSum(root, l, r):
            # range가 정확히 일치한다면 total 값이 곧 sum임
            if root.start == l and root.end == r:
                return root.total
            mid = getMid(root.start, root.end)
            # range의 right가 mid보다 작다면, 전체 구간은 left subtree에 위치
            if r <= mid:
                return rangeSum(root.left, l, r)
            # range의 left가 mid보다 크다면, 전체 구간은 right subtree에 위치
            elif l >= mid + 1:
                return rangeSum(root.right, l, r)
            # 둘 다 아니라면 구간이 쪼개진 것. 구간합을 쪼개서 계산해야 함.
            else:
                return rangeSum(root.left, l, mid) + rangeSum(root.right, mid+1, r)
        return rangeSum(self.root, l, r)
```

