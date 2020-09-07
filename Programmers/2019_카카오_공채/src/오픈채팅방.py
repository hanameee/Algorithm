from collections import defaultdict


def solution(record):
    answer = []
    d = defaultdict(str)
    for i in range(len(record)):
        record[i] = record[i].split()
        if record[i][0] != "Leave":
            d[record[i][1]] = record[i][2]
    for r in record:
        if r[0] == "Enter":
            answer.append(f'{d[r[1]]}님이 들어왔습니다.')
        elif r[0] == "Leave":
            answer.append(f'{d[r[1]]}님이 나갔습니다.')
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
