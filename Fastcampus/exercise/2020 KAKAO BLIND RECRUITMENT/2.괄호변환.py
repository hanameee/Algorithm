import sys
input = sys.stdin.readline
p = input().strip()


# 올바른 괄호 문자열이면 True, 아니면 False
def check_valid(s):
    stack = []
    for i in range(len(s)):
        if stack:
            if stack[-1] == "(" and s[i] == ")":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if stack:
        return False
    else:
        return True


# u의 끝 idx를 리턴
def get_split_idx(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def flip(s):
    result = ""
    for i in range(len(s)):
        if s[i] == "(":
            result += ")"
        else:
            result += "("
    return result


# u가 올바른 괄호 문자열이 아닐 때 v가 재귀적으로 겪는 함수
def process(s):
    if len(s) == 0:
        return("")
    idx = get_split_idx(s)
    u = s[:idx+1]
    v = s[idx+1:]
    if check_valid(u):
        temp = u
        result = process(v)
        return (temp + result)
    else:
        temp = "("
        result = process(v)
        temp = temp + result + ")" + flip(u[1:len(u)-1])
        return temp


if check_valid(p):
    print(p)
else:
    result_string = ""
    idx = get_split_idx(p)
    u = p[:idx+1]
    v = p[(idx+1):]
    # u가 올바른 괄호 문자열일 경우
    if check_valid(u):
        result_string += u
        result_string += process(v)
    # u가 올바른 괄호 문자열이 아닐 경우
    else:
        temp = "("
        temp += process(v) + ")" + flip(u[1:len(u)-1])
        result_string += temp
    print(result_string)
