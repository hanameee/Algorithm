import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input().strip())


for _ in range(test_case):
    commands = input().strip()
    n = int(input().strip())
    data = input().strip()
    arr = []
    # 데이터 배열 완성하기
    if len(data) == 2:
        arr = []
    else:
        num = ""
        for i in range(1, len(data)-1):
            if data[i] == ",":
                arr.append(int(num))
            else:
                if data[i-1] != ",":  # 연속된 수인 경우
                    num += data[i]
                else:
                    num = data[i]
        arr.append(int(num))
    # 함수 수행하기
    data_deque = deque(arr)
    error_flag = False
    is_reverse = False
    for c_idx in range(len(commands)):
        c = commands[c_idx]
        if c == "D":
            if len(data_deque) == 0:
                print("error")
                error_flag = True
                break
            if is_reverse:
                data_deque.pop()
            else:
                data_deque.popleft()
        else:
            is_reverse = not is_reverse
    if not error_flag:
        answer = list(data_deque)
        if not is_reverse:
            answer = "[" + ','.join(map(str, answer)) + "]"
            print(answer)
        else:
            answer.reverse()
            answer = "[" + ','.join(map(str, answer)) + "]"
            print(answer)
