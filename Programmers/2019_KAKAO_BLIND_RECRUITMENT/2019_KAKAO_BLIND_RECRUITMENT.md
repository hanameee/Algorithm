# 2019_KAKAO_BLIND RECRUITMENT

## 1. 오픈채팅방

대략 13분? 컷

닉네임이 변경될때마다 dict의 value 값을 바꿔주고, 마지막에는 enter, leave만 uid를 dict에서 찾아서 그대로 프린트해줌.

Enter 할 때도 닉네임이 바뀌는걸 고려 안해서 살짝 디버깅.

## 2. 실패율

33분 컷

이것도 대따 쉬운 문제인데 변수 이름을 헷갈리게 잡아서 디버깅했다. 흑흑...멍청아... 30분이나 쓰면 안되는 문제.

## 3. 후보키

거의 1시간 반 넘게 붙들고 있었다.

또..삽질..나는야 삽질 마스따...
이래서 코드가 길어지면 함수를 분리하라고 하는거겠지? 3중 포문 나오기 시작하면 귀찮아도 함수 분리하자.

`1,2` 가 valid key일 때

```python
# 12:45~
from itertools import combinations


def solution(relation):
    keys = set([col for col in range(len(relation[0]))])
    original_rows = len(relation)
    valid_key = []
    i = 1
    while i <= len(keys):
        set_rows = set([])
        candidate_keys = combinations(keys, i)
        for candidate_key in candidate_keys:
            toContinue = False
            # 기존 v_keys 중 하나라도 candidate_key에 포함되어 있으면
            # print(valid_key, candidate_key)
            for v_keys in valid_key:
              	# 얘의 range를 잘못 두었다.
                chk = True
                for v in v_keys:
                    if v not in candidate_key:
                        chk = False
                        break
                # 지금 보는 combination이 이번 v_key를 포함한다는 뜻
                if chk:
                    toContinue = True
                    break
            if toContinue:
                continue
            for row in relation:
                value = ""
                for key in candidate_key:
                    value += ","+row[key]
                set_rows.add(value)
            if original_rows == len(set_rows):
                valid_key.append(candidate_key)
            set_rows = set([])
        i += 1
    answer = valid_key
    return len(answer)


# print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
#       "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
print(solution([["1", "1", "1", "2"],
                ["2", "1", "2", "3"],
                ["3", "2", "1", "2"]]))
```



## 4. 무지의 먹방 라이브

어렵누...ㅠ 거의 오늘 하루종일 붙들고 있었네 ^^
내가 생각한건, 음식들을 최소값으로 정렬하고 그 음식들을 다 먹었을 때 단위로 생각하는 것. 

근데 음식들을 정렬했을 때 원래의 순서를 기억하는 것이 어려웠다.
하나의 적당한 복잡도를 가지는 예제를 가지고 꼼꼼히 써가면서 규칙을 정리하는 것이 중요한 것 같다.

답을 찾아보니 다음과 같다.

`모범 답안`

제일 적은 시간이 걸리는 음식들부터 먹어야 한다. 여기서 **minHeap** 을 생각했으면 좋았겠지?

값이 n가장 작은 친구가 m의 시간이 걸린다면, 한 사이클의 단위는 n이다.
그리고 한 사이클을 돌 때마다 시간은 n*m 만큼 늘어난다.

그렇다면, 알고리즘은 아래처럼

1. 배열의 한 사이클 크기(n)를 구한다.
2. k가 만약 배열의 min값*n 이상이라면 (사이클을 돌아도 k가 남으면) 배열 수 전체가 min값만큼 줄어들고, 그 수는 사라진다. 나머지 순서는 유지한다.
3. k가 배열의 min값*n 미만이라면... (k% 사이클 이후의 음식번호) 를 반환한다

```python
import heapq


def solution(food_times, k):
    # 음식 크기, 원래 위치로 food_times를 재정의한다. (list comprehension 사용 - 첫 index를 1로 정의해 줄 수 있다.)
    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    heapq.heapify(food_times)
    # 가장 크기가 작은 음식의 크기
    min_food_size = food_times[0][0]
    prev_food_size = 0
    # 사이클을 돌 수 있을때까지 돈다 (남은 k가 한 사이클에 해당하는 음식 크기*현재 남은 음식 보다 크다면 사이클을 돌 수 있다는 것)
    while k - ((min_food_size - prev_food_size) * len(food_times)) >= 0:
        # 사이클을 도는데까지 걸린 시간만큼 k 차감
        k -= (min_food_size - prev_food_size) * len(food_times)
        # k를 줄여주기 위해 prev_
        prev_food, idx = heapq.heappop(food_times)
        # 아직 k가 남았는데 음식을 다먹었다면
        if not food_times:
            return -1
        # 가장 작은 food는 pop하고 난 다음 heap의 제일 처음에 위치한 친구
        min_food_size = food_times[0][0]
    # 사이클을 다 돌고, 이제 이 사이클에서 k가 끝나게 됨
    # 이제는 남은 음식들을 처음에 enumerate를 통해 재정의했었던 key로 정렬해주면 됨
    food_times = sorted(food_times, key=lambda x: x[1])
    # 주의 - 원판을 한번 도는 것과 사이클을 도는 것은 다르다
    return food_times[k % len(food_times)][1]


# print(solution([2, 1, 1, 1, 2, 5, 3], 13))  # 6이 나와야 함
print(solution([3, 1, 2], 5))  # 1이 /나와야 함
```

위 풀이 하면 틀림...뭐지...뭐 실수했지..다시 찾아보기

Heapq 안쓰고 그냥 sort 해도 되긴 되는구나...정말 놀랍따..

```python
def solution(food_times, k):
    times = {}
    for idx, time in enumerate(food_times):
        if time in times:
            times[time].append(idx)
        else:
            times[time] = [idx]

    len_foods = len(food_times)
    cycle = 0
    for time in sorted(times):
        if k - (len_foods*(time-cycle)) >= 0:
            k -= len_foods*(time-cycle)
            len_foods -= len(times[time])
            cycle += time-cycle
        else:
            k %= len_foods
            for i in times:
                if i >= time:
                    idx = times[i][0]
                    break
            for i in range(idx, len(food_times)):
                if food_times[i] >= time:
                    if k == 0:
                        return i+1
                    k -= 1
    return -1
    
```



## 길 찾기 게임

파이썬에서의 class 사용과 트리/전위순위/후위순위를 복습할 수 있었던 문제.
카카오 코테는 어렵고 힘들지만 재밌다. 문제를 어쩜 이렇게 풀락말락 재밌게 내주시는지 ^_^...

```python
import sys
sys.setrecursionlimit(10**6)


# 길 찾기 게임
class Node(object):
    def __init__(self, x, data):
        self.data = data
        self.left = None
        self.right = None
        self.x = x


pre_lst = []
post_lst = []


def pre_order(node):
    global pre_lst
    pre_lst.append(node.data)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


def post_order(node):
    global post_lst
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    post_lst.append(node.data)


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x, data):
        self.root = self.insert_value(self.root, x, data)
        return self.root is not None

    def insert_value(self, node, x, data):
        # 자식이 없다면 그 자리에 데이터를 삽입한다
        if node is None:
            node = Node(x, data)
        else:
            if x <= node.x:
                node.left = self.insert_value(node.left, x, data)
            else:
                node.right = self.insert_value(node.right, x, data)
        return node

    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)


def solution(nodeinfo):
    global pre_lst, post_lst
    nodeinfo = [value+[idx+1] for idx, value in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    bst = BinaryTree()
    for node_idx in nodeinfo:
        bst.insert(node_idx[0], node_idx[2])
    pre_order(bst.root)
    post_order(bst.root)
    answer = [pre_lst, post_lst]
    return answer
```

