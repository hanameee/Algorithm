# 10:55~
from string import ascii_lowercase
from collections import Counter
alpha_list = ascii_lowercase


def filter_alpha_lst(lst):
    new_list = []
    for e in lst:
        flag = True
        for char in e:
            if char not in alpha_list:
                flag = False
        if not flag:
            continue
        new_list.append(e)
    return new_list


def get_alpha_lst(a):
    lst = []
    for i in range(len(a)-1):
        lst.append(a[i]+a[i+1])
    return lst


def compare(a_lst, b_lst):
    count = 0
    sum_count = 0
    dup_count = 0
    a_set = set(a_lst)
    len_a = len(a_lst)
    len_b = len(b_lst)
    for e in a_set:
        count_a = a_lst.count(e)
        count_b = b_lst.count(e)
        # 다중 중복요소라면
        if count_a >= 1 and count_b >= 1:
            sum_count += max(count_a, count_b)
            dup_count += min(count_a, count_b)
            len_a -= count_a
            len_b -= count_b
        # 일반 요소라면
    return (dup_count, sum_count + len_a + len_b)

    dup_count += 1
    if e in b_lst:
        count += 1
    return count


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    lst1 = get_alpha_lst(str1)
    lst1 = filter_alpha_lst(lst1)
    lst2 = get_alpha_lst(str2)
    lst2 = filter_alpha_lst(lst2)
    inter = Counter(lst1) & Counter(lst2)
    union = Counter(lst1) | Counter(lst2)
    print(inter, union)
    if len(union) == 0:
        jkd = 1
    else:
        jkd = len(inter) / len(union)

    answer = int(jkd*65536)
    return answer


# print(solution("aaaabcd", "aaaaaaabfg"))
print(solution("aa1+aa2", "AAAA12"))
