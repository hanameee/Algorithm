N = input()
N_dict = {int(value): int(value) for value in input().split()}
M = input()
M_list = list(map(int, input().split(" ")))
for item in M_list:
    try:
        answer = N_dict[item]
        print(1)
    except KeyError:
        print(0)
