from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    c_dict = defaultdict(int)
    answer = []
    for c in course:
        for order in orders:
            if len(order) >= c:
                keys = list(combinations(sorted(list(order)), c))
                for key in keys:
                    c_dict[key] += 1

    best_menu_count = [2 for _ in range(11)]
    best_menu = [[] for _ in range(11)]

    for k, v in c_dict.items():
        if best_menu_count[len(k)] < v:
            best_menu_count[len(k)] = v
            best_menu[len(k)] = [k]
        elif best_menu_count[len(k)] == v:
            best_menu[len(k)].append(k)

    for menus in best_menu:
        if len(menus):
            for m in menus:
                answer.append(''.join(m))
    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
