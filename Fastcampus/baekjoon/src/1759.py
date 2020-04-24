from collections import deque
l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
vowels = ["a", "e", "i", "o", "u"]


def check_rule(password):
    global vowels
    v_flag = 1
    c_flag = 2
    for char in password:
        if char in vowels:
            v_flag -= 1
        else:
            c_flag -= 1
        if v_flag <= 0 and c_flag <= 0:
            return True
    return False


def make_password(char_idx):
    global alpha, vowels, l, c
    q = deque([])
    q.append((alpha[char_idx], char_idx))
    while q:
        password, idx = q.popleft()
        if len(password) == l:
            if check_rule(password):
                print(password)
        else:
            for c_idx in range(idx+1, len(alpha)-(l-len(password))+1):
                if alpha[c_idx] not in password:
                    q.append((password+alpha[c_idx], c_idx))


for i in range(len(alpha)-(l-1)):
    make_password(i)
