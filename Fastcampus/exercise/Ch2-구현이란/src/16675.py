data = list(input().split())
MS = list(set(data[:2]))
TK = list(set(data[2:]))


def rsp(ms, tk):
    # 둘다 같은 걸 냈을 때
    if len(ms) == len(tk) == 1:
        if ms[0] == "R":
            if tk[0] == "S":
                return "MS"
            if tk[0] == "P":
                return "TK"
        if ms[0] == "S":
            if tk[0] == "P":
                return "MS"
            if tk[0] == "R":
                return "TK"
        if ms[0] == "P":
            if tk[0] == "R":
                return "MS"
            if tk[0] == "S":
                return "TK"
        return "?"
    # ms만 한개를 냈을 때
    if len(ms) == 1:
        if ms[0] == "R":
            if "P" in tk:
                return "TK"
        if ms[0] == "S":
            if "R" in tk:
                return "TK"
        if ms[0] == "P":
            if "S" in tk:
                return "TK"
        return "?"
    # tk만 한개를 냈을 때
    if len(tk) == 1:
        if tk[0] == "R":
            if "P" in ms:
                return "MS"
        if tk[0] == "S":
            if "R" in ms:
                return "MS"
        if tk[0] == "P":
            if "S" in ms:
                return "MS"
        return "?"
    return "?"


print(rsp(MS, TK))
