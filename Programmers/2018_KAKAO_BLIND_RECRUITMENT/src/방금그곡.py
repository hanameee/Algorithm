# 1:10~


def parse_melody(m):
    idx = 0
    lst = []
    acc = ""
    while idx < len(m):
        # 그냥 음이면
        if m[idx] != "#":
            # 전 음이 있었다면
            if acc:
                lst.append(acc)
                acc = ""
        acc += m[idx]
        idx += 1
    if acc:
        lst.append(acc)
    return lst


def solution(m, musicinfos):
    parsed_m = parse_melody(m)
    m_info = []
    # m과 musicinfo를 음단위로 파싱해서 리스트에 넣기
    for info in musicinfos:
        info = info.split(",")
        s_time = int(info[0][:2])*60 + int(info[0][3:])
        e_time = int(info[1][:2])*60 + int(info[1][3:])
        playtime = e_time - s_time
        melody = parse_melody(info[-1])
        m_info.append([playtime, info[2], melody])
    # 음악별로 시간을 이용해 라디오에서 재생된 멜로디 전체를 구성하기
    for info in range(len(m_info)):
        new_melody = []
        for i in range(m_info[info][0]):
            if i >= len(m_info[info][-1]):
                new_melody.append(m_info[info][-1][i % len(m_info[info][-1])])
            else:
                new_melody.append(m_info[info][-1][i])
        m_info[info][-1] = new_melody
    # m과 멜로디들을 비교하기
    ans_lst = []
    for info in range(len(m_info)):
        flag = False
        idx = 0
        while idx+len(parsed_m) <= len(m_info[info][-1]):
            if m_info[info][-1][idx] == parsed_m[0]:
                if m_info[info][-1][idx:idx+len(parsed_m)] == parsed_m:
                    flag = True
                    break
            idx += 1
        if flag:
            ans_lst.append(m_info[info])
    # 일치하면 일치하는 시간을 찾고, 시간도 일치하면 먼저 입력된애를 반환
    if len(ans_lst) == 1:
        return(ans_lst[0][1])
    elif len(ans_lst) == 0:
        return "(None)"
    else:
        ans_lst.sort(key=lambda x: -x[0])

        return(ans_lst[0][1])


# print(
#     solution("ABC", ["12:00,12:11,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF", "13:00,13:14,NANA,ABCDEF"]))
# print(
#     solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABCDEFG", ["11:45,12:01,HELLO,CDEFGAB",
                           "13:00,13:05,WORLD,ABCDEF"]))

# print(solution("CC#BCC#BCC#BCC#B", [
#     "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
