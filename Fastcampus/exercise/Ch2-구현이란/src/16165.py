import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gg_dict = {}
for _ in range(n):
    gg_name = input().strip()
    gg_dict[gg_name] = []
    gg_member_num = int(input())
    for _ in range(gg_member_num):
        gg_dict[gg_name].append(input().strip())

for _ in range(m):
    quiz_name = input().strip()
    quiz_type = int(input())
    if not quiz_type:
        gg_dict[quiz_name].sort()
        for member in gg_dict[quiz_name]:
            print(member)
    else:
        for gg in gg_dict.keys():
            if quiz_name in gg_dict[gg]:
                print(gg)
