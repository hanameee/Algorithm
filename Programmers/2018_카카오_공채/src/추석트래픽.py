import heapq


def solution(lines):
    for idx in range(len(lines)):
        line = lines[idx]
        linearr = line.split(" ")
        linearr[1] = linearr[1].replace(".", ":").split(":")
        linearr[1] = int(linearr[1][3])/1000+int(linearr[1][2]) + \
            int(linearr[1][1])*60+int(linearr[1][0])*60*60
        lines[idx] = (linearr[1]-float(linearr[2][0:-1]) +
                      0.001, float(linearr[2][0:-1]))
    lines = sorted(lines, key=lambda x: x[0])
    max_cap = 0
    q = []
    for line in lines:
        heapq.heappush(q, sum(line)-0.001)
        startTime = line[0]
        while q:
            endTime = heapq.heappop(q)
            if endTime >= round(startTime-1+0.001, 3):
                heapq.heappush(q, endTime)
                break
        max_cap = max(max_cap, len(q))
    return max_cap


print(solution(["2016-09-15 01:00:04.002 2.0s",
                "2016-09-15 01:00:07.000 2s"]))
# print(solution([
#     "2016-09-15 20:59:57.421 0.351s",
#     "2016-09-15 20:59:58.233 1.181s",
#     "2016-09-15 20:59:58.299 0.8s",
#     "2016-09-15 20:59:58.688 1.041s",
#     "2016-09-15 20:59:59.591 1.412s",
#     "2016-09-15 21:00:00.464 1.466s",
#     "2016-09-15 21:00:00.741 1.581s",
#     "2016-09-15 21:00:00.748 2.31s",
#     "2016-09-15 21:00:00.966 0.381s",
#     "2016-09-15 21:00:02.066 2.62s"
# ]))
