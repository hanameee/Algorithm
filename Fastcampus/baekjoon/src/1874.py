n = int(input())
data = list()
for i in range(n):
    data.append(int(input()))

stack = list()
result = list()

pointer = 1
data_index = 0

while data_index < n:
    target = data[data_index]
    # in 연산이 아닌 단순 비교연산으로 수정
    if pointer <= target:
        stack.append(pointer)
        pointer += 1
        result.append("+")
    elif stack[-1] == target:
        stack.pop()
        data_index += 1
        result.append("-")
    else:
        print("NO")
        exit(0)

print("\n".join(result))
