class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.parent = -1


def in_order(node, level):
    global level_depth, idx
    level_depth = max(level, level_depth)
    if node.left != -1:
        in_order(tree[node.left], level+1)
    level_min[level] = min(level_min[level], idx)
    level_max[level] = max(level_max[level], idx)
    idx += 1
    if node.right != -1:
        in_order(tree[node.right], level+1)


N = int(input())
tree = {}
level_min = [N]
level_max = [0]
level_depth = 1
idx = 1
# Tree 초기화
for i in range(1, N+1):
    tree[i] = Node(i, -1, -1)
    level_min.append(N)
    level_max.append(0)

# Input 받아 tree 만들기
for _ in range(N):
    value, left, right = map(int, input().split())
    tree[value].left = left
    tree[value].right = right
    if left != -1:
        tree[left].parent = value
    if right != -1:
        tree[right].parent = value

for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

answer = [1, level_max[i]-level_min[i]+1]

for i in range(2, N+1):
    if answer[1] < level_max[i]-level_min[i] + 1:
        answer[0] = i
        answer[1] = level_max[i]-level_min[i] + 1

print(answer[0], answer[1])
