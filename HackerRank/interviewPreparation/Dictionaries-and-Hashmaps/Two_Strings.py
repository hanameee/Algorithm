# Complete the twoStrings function below.


def twoStrings(s1, s2):
    ss1 = set(s1)
    ss2 = set(s2)
    ss12 = set(s1+s2)
    if len(ss1)+len(ss2) != len(ss12):
        return "YES"
    return "NO"


q = int(input())

for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)
    print(result)
