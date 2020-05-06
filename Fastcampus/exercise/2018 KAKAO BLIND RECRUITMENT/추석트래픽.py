# b가 무조건 나중 수
def is_in_range(a, b):
    a_sec = a[0]*3600 + a[1]*60 + a[2]/1000
    b_sec = b[0]*3600 + b[1]*60 + b[2]/1000
    print(a, b, a_sec, b_sec, "a,b")
    if b_sec - a_sec <= 1:
        return True
    else:
        print(False)
        return False


def solution(lines):
    count = 0
    s_idx = 0
    e_idx = 0
    max_count = 0
    q = []
    popped = [0]*2000
    for line in lines:
        hh = int(line[11:13])
        mm = int(line[14:16])
        ss = int(line[17:19])*1000
        ss += int(line[20:23])
        t = int(line[24])*1000 - 1
        if len(line[26:-1]) == 3:
            t += int(line[26:-1])
        elif len(line[26:-1]) == 2:
            t += int(line[26:-1]) * 10
        elif len(line[26:-1]) == 1:
            t += int(line[26:-1]) * 100
        end_time = [hh, mm, ss]
        q.append(end_time)
        if ss - t <= 0:
            if mm == 0:
                hh -= 1
                mm = 59
            ss = (ss-t) + 60000
            mm = mm-1
        else:
            ss -= t
        start_time = [hh, mm, ss]
        count += 1
        e_idx += 1
        # 존재하는 로그가 있다면
        print(q)
        if len(q) > 1:
            for idx in range(len(q)-1):
                # end_time이 limit보다 작으면 pop
                if not is_in_range(q[idx], start_time) and not popped[idx]:
                    count -= 1
                    popped[idx] = 1
        max_count = max(count, max_count)
    answer = max_count
    print(max_count)
    return max_count


# solution(
#     [
#         "2016-09-15 01:00:04.002 2.0s",
#         "2016-09-15 01:00:07.000 3s"
#     ]
# )
solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    '2016-09-15 21:00:00.748 2.31s',
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s",
])
