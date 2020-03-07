# Tree

### 트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조

이진 탐색 트리 (BST) 의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용된다.

### LinkedList로 BST 구현하기

```python
# 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        # 순회한다
        while True:
            # 새로운 놈은 지금 놈의 왼쪽으로 가야함
            if value < self.current_node.vaule:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
            
```

### BST 탐색 메소드 구현하기

(위의 코드와 연결됨... 🚀)

```python
    def search(self, value):
        self.current_node = self.head
        # self.current_node가 None이 되면 반복문을 종료한다
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
      
head = Node(1)   
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.search(9) # False
```

### BST 삭제 메소드 구현하기

```python
    def delete(self, value):
        # 삭제할 노드가 트리에 존재하는지 검색하는 코드
        searched = False
        self.current_node = self.head
        self.parent = self.head

        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if not searched:
            return False

        # 이후부터 케이스를 분리해서 코드 작성
        # case 1 - 삭제할 node가 leaf node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        # case 2-1 - 삭제할 node의 child node가 1개일 경우 (왼쪽 child)
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
            del self.current_node
        # case 2-2 - 삭제할 node의 child node가 1개일 경우 (오른쪽 child)
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
            del self.current_node
        # case 3-1 - 삭제할 node의 child node가 2개일 경우
        elif self.current_node.left != None and self.current_node.right != None:
            self.change_node_parent = self.current_node.right
            self.change_node = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            if value < self.parent.value:
                self.parent.left = self.change_node
            else:
                self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
```

### 전체 BST 코드 테스트

```python
# 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left == None:
                    self.current_node.left = Node(value)
                    break
                else:
                    self.current_node = self.current_node.left
            else:
                if self.current_node.right == None:
                    self.current_node.right = Node(value)
                    break
                else:
                    self.current_node = self.current_node.right

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if value == self.current_node.value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        # 삭제할 노드가 트리에 존재하는지 검색하는 코드
        searched = False
        self.current_node = self.head
        self.parent = self.head

        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if not searched:
            return False

        # 이후부터 케이스를 분리해서 코드 작성
        # case 1 - 삭제할 node가 leaf node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        # case 2-1 - 삭제할 node의 child node가 1개일 경우 (왼쪽 child)
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
            del self.current_node
        # case 2-2 - 삭제할 node의 child node가 1개일 경우 (오른쪽 child)
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
            del self.current_node
        # case 3-1 - 삭제할 node의 child node가 2개일 경우
        elif self.current_node.left != None and self.current_node.right != None:
            self.change_node_parent = self.current_node.right
            self.change_node = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            if value < self.parent.value:
                self.parent.left = self.change_node
            else:
                self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
            
# 1-999 까지의 숫자 중 임의로 100개를 추출해서 이진 탐색 트리에 입력, 검색, 삭제
import random
bst_nums = set()

while len(bst_nums) != 100:
    bst_nums.add(random.randint(0,999))

head = Node(500)
BST = NodeMgmt(head)

for num in bst_nums:
    BST.insert(num)

for num in bst_nums:
    if BST.search(num) == False:
        print("search failed", num)

delete_nums = set()
bst_nums = list(bst_nums) # set 타입을 list 타입으로 변환

while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0,99)])

print(delete_nums)

for num in delete_nums:
    BST.delete(num)

for num in bst_nums:
    if BST.search(num) == False:
        print("search failed", num)
```

### 시간복잡도

depth의 깊이 만큼의 시간복잡도를 가짐.
데이터가 2개일때는 depth가 1, 4개일때는 2, 16개일때는 4, 256개일때는 8....
n에 따라 depth 가 밑이 2인 log 만큼의 깊이를 가지므로 트리는 O(log n) 의 시간복잡도를 가진다.

그러나 이는 BST가 balanced 되어 있을 경우의 일반적인 복잡도이며 최악의 경우 Tree는 linked list와 같은 O(n) 의 시간 복잡도를 가진다.