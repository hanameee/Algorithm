# 11:56~


def solution(record):
    id_name = dict()
    record_lst = []
    for r in record:
        r_lst = r.split()
        if len(r_lst) == 3:
            id_name[r_lst[1]] = r_lst[2]
        if r_lst[0] != "Change":
            record_lst.append([r_lst[0], r_lst[1]])
    for r in range(len(record_lst)):
        command, uid = record_lst[r]
        if command == "Enter":
            record_lst[r] = id_name[uid]+"님이 들어왔습니다."
        else:
            record_lst[r] = id_name[uid]+"님이 나갔습니다."
    answer = record_lst

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
                "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
