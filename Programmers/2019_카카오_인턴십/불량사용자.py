lst = []
count = 0
check_same = [False]*1024


# 확인하기
def dfs(cur):
    global count, check_same, lst
    if len(cur) == len(lst):
        value = 0
        for i in cur:
            value += 2**(i)
        if check_same[value] == False:
            count += 1
            check_same[value] = True
        return
    for j in lst[len(cur)]:
        if j not in cur:
            new_cur = cur + [j]
            dfs(new_cur)


# 후보 아이디인지 판별하기
def is_valid(uid, bid):
    if len(uid) != len(bid):
        return False
    for b_idx in range(len(bid)):
        if bid[b_idx] != "*":
            if uid[b_idx] != bid[b_idx]:
                return False
    return True


def solution(user_id, banned_id):
    # 후보군 만들기
    for qry in banned_id:
        user_lst = []
        for user in range(len(user_id)):
            if is_valid(user_id[user], qry):
                user_lst.append(user)
        lst.append(user_lst)
    for i in lst[0]:
        dfs([i])
    answer = count
    return answer


print(solution(["frodo", "fradi", "crodo",
                "abc123", "frodoc"],	["fr*d*", "abc1**"]))
