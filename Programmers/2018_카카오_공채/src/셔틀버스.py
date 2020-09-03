import heapq


def solution(n, t, m, timetable):
    curr_time = 540
    for i in range(len(timetable)):
        time = timetable[i]
        timetable[i] = int(time[:2])*60+int(time[3:])
    heapq.heapify(timetable)
    latest_time = curr_time
    for i in range(n):
        count = 0
        while count < m and timetable:
            curr_person = heapq.heappop(timetable)
            if curr_person <= curr_time:
                count += 1
                continue
            else:
                heapq.heappush(timetable, curr_person)
                break
        if count < m:
            latest_time = curr_time
        else:
            latest_time = curr_person-1
        curr_time += t
    answer = '{:02d}:{:02d}'.format(*divmod(latest_time, 60))
    return answer


print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
