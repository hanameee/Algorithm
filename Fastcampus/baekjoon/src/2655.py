import sys
n = int(sys.stdin.readline().strip())
data = [[] for i in range(n)]

for i in range(n):
    # 넓이, 높이, 무게
    data[i] = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(n+1)]  # height sum
blocks = [[] for i in range(n+1)]

print(data)
for i in range(n):
    index_i = i+1
    if dp[index_i] == 0:
        max_area, height, max_weight = data[i]
        lis = [index_i]
        for j in range(n):
            index_j = j+1
            if i != j:
                a, h, w = data[j]
                if a <= max_area and w <= max_weight:
                    lis.append(index_j)
                    # max_area, max_weight = a, w
        height_sum = 0
        for block_idx in lis:
            height_sum += data[block_idx-1][1]
        for block_idx in lis:
            dp[block_idx] = 1
        dp[index_i] = height_sum
        blocks[index_i] = lis

result = 0
result_index = 0

for i in range(1, n+1):
    if dp[i] > result:
        result = dp[i]
        result_index = i

# for block in blocks:
#     print(block)
# print(len(blocks[result_index]))
# blocks[result_index].reverse()
# for block in blocks[result_index]:
#     print(block)
