from copy import deepcopy


def check_valid(x, y, a, b, bt):
    # 삭제하기
    if b == 0:
        temp_bt = deepcopy(bt)
        temp_bt.pop(bt.index([x, y, a]))
        for x_, y_, a_ in bt:
            if x_ == x and y_ == y and a == a_:
                continue
            if not check_valid(x_, y_, a_, 1, temp_bt):
                return False
            else:
                temp_bt.append([x_, y_, a_])
        return True
    # 설치하기
    else:
        # 보 설치
        if a:
            if [x, y-1, 0] in bt or [x+1, y-1, 0] in bt or ([x-1, y, 1] in bt and [x+1, y, 1] in bt):
                return True
        # 기둥 설치
        else:
            if y == 0 or [x-1, y, 1] in bt or [x, y, 1] in bt or [x, y-1, 0] in bt:
                return True
    return False


def solution(n, build_frame):
    built_frame = []
    # x가 열, y가 행
    for order in build_frame:
        x, y, a, b = order
        if check_valid(x, y, a, b, built_frame):
            if b == 1:
                built_frame.append([x, y, a])
            else:
                built_frame.pop(built_frame.index([x, y, a]))
    answer = built_frame
    answer.sort()
    return answer


# solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [
#          5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
print(solution(5,	[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
