# LinkedList

### 클래스로 LinkedList 구현하기

```python
class Node:
    def __init__(self,data,next=None):
        self.next = next
        self.data = data

# 초기값 추가
node1 = Node(1)
head = node1

# 맨 마지막에 데이터 추가하기
def add(data):
    node = head
    while node.next:
        node = node.next
        # 마지막 노드의 포인터값에 새로운 노드 추가
    node.next = Node(data)

# 전체 리스트 데이터 출력하기
def desc():
    node = head
    while node.next:
        print(node.data)
        node = node.next
    print(node.data)

# 링크드 리스트에 데이터 추가하기
for index in range(2,11):
    add(index)

# 노드 사이에 데이터 추가하기
node2 = Node(3.5)
node = head
search = True
while search:
    if node.data == 3:
        search = False
    else:
        node = node.next
temp = node.next
node.next = node2
node2.next = temp
```

### 객체지향 문법으로 구현한 LinkedList

```python
# 객체지향 문법으로 구현하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    # Mgmt 를 Init 할때 입력한 데이터로 노드를 만들고 그 노드를 head 로 설정
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        # 만약 Mgmt 할때 head가 설정되지 않았을 경우를 대비한 방어코드
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)
        
    def delete(self,data):
        # 리스트에 데이터가 없을 때 (head가 없을 때)
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다")
            return
        # 삭제할 데이터가 head일 때
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            print("삭제되었습니다")
            return
        # 삭제할 데이터가 head가 아닐 때
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    print("삭제되었습니다")
                    return
                else:
                    node = node.next
            # 끝가지 탐색했지만 data가 발견되지 않았을 때
            print("해당 값을 가진 노드가 없습니다")
            
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                print("%d를 찾았습니다" % data)
                print(node, node.data)
                return
            else:
                node = node.next
        print("해당 데이터가 존재하지 않습니다")
        return
      
linkedList1 = NodeMgmt(1)
for index in range(2,11):
    linkedList1.add(index)
linkedList1.delete(1)
linkedList1.desc()
linkedList1.find(1)
```

### Double Linked List 구현하기

```python
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = Node(data)

    def insert(self, data):
        if self.head == '':
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == "":
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == "":
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    # 특정 값(before_data)을 가진 노드 앞에 데이터 삽입하기
    def insert_before(self, data, before_data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            # 원래 자리에 있던 노드를 한칸 앞으로 밀기 위해 before_new 에 저장
            before_new = node.prev
            # before_new 다음에 new 인 관계 - 서로 연결
            before_new.next = new
            new.prev = before_new
            # new 다음에 node 인 관계 - 서로 연결
            new.next = node
            node.prev = new

    # 특정 값(after_data)을 가진 노드 뒤에 데이터 삽입하기
    def insert_after(self, data, after_data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            # 원래 자리에 있던 노드를 한칸 뒤로 밀기 위해 after_new 에 저장
            after_new = node.next
            # new 다음에 after_new 인 관계 - 서로 연결
            new.next = after_new
            after_new.prev = new
            # node 다음에 new 인 관계 - 서로 연결
            new.prev = node
            node.next = new


double_linked_list = NodeMgmt(1)
for index in range(2,11):
    double_linked_list.insert(index)
double_linked_list.insert_before(2.5,3)
double_linked_list.insert_after(3.5,3)
double_linked_list.desc()

```

