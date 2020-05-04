import heapq
from copy import deepcopy

k, n = map(int, input().split())
p_list = list(map(int, input().split()))

# lst는 heap, ck는 중복된 수를 포함하지 않겠다는 의미 2*2*3, 2*3*2는 같은 수니까.
lst, ck = deepcopy(p_list), set()

heapq.heapify(lst)  # 배열을 heap으로 바꾼다.
ith = 0


while ith < n:
    mn = heapq.heappop(lst)  # 꼭대기 값, 즉 가장 작은 값
    if mn in ck:
        continue  # 중복되는 값이면 카운트 안함
    ith += 1
    ck.add(mn)
    for i in p_list:
        # heap에 어떤 식으로 수를 넣어줄지가 제일 중요함.
        if mn * i < 2**31:
            heapq.heappush(lst, mn*i)
print(mn)
