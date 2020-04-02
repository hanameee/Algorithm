from collections import deque
import sys

MAX = 100001
array = [0] * MAX
n, k = map(int, sys.stdin.readline().split())


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        # 이동할 수 있는 거리가 3가지 뿐이기에, 3가지 경우로 다음 정점들을 해결할 수 있음
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            # 범위에 포함되어 있고 방문하지 않았다면
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                # 최소시간에 대한 정보를 array에 담아주고
                # 다시 q에 넣어줘서 반복적으로 dfs 수행
                q.append(next_pos)


print(bfs())
