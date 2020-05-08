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


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
                [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
