import sys
input = sys.stdin.readline
n = int(input())
result = 0
column, left_diagonal, right_diagonal = [
    False]*n, [False]*(2*n-1), [False]*(2*n-1)


def check(i):
    global result
    if i == n:
        result += 1
        return
    for j in range(n):
        # 셋 중 하나라도 False라면
        if not (column[j] or left_diagonal[i+j] or right_diagonal[i-j+n-1]):
            column[j] = left_diagonal[i+j] = right_diagonal[i-j+n-1] = True
            check(i+1)
            column[j] = left_diagonal[i+j] = right_diagonal[i-j+n-1] = False


check(0)
print(result)

# def check(x):
#     for i in range(x):
#         if row[x] == row[i]:
#             return False
#         if abs(row[x] - row[i]) == x-i:
#             return False
#     return True


# def dfs(x):
#     global result
#     if x == n:
#         result += 1
#     else:
#         for i in range(n):
#             row[x] = i
#             if check(x):
#                 dfs(x+1)


# n = int(input())
# row = [0]*n
# result = 0
# dfs(0)
# print(result)
