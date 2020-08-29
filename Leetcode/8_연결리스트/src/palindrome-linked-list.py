from collections import deque


def solution(head):
    q = deque([])
    if not head:
        return True
    node = head
    while node is not None:
        q.append(node.val)
        q = node.next
    while len(q) > 1:
        if q.pop() != q[-1]:
            return False
    return True


solution()
