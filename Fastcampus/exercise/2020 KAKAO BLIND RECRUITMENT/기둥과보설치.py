from copy import deepcopy


# 조건 확인 (mp의 x,y에 대해 type을 설치 할 수 있는가)
def is_valid(x, y, mp, t):
    # 기둥이라면
    if t == 0:
        # 바닥이거나, 양옆 중 한쪽에 보가 있거나, 아래쪽에 기둥이 있거나
        if x == 0 or (y>0 and mp[x][y-1][1]) or mp[x][y+1][1] or (x>0 and mp[x-1][y][0]):
            return True
        else:
            return False
    # 보라면
    else:
        # 양옆 중 한쪽에 기둥 설치되어 있거나, 양쪽에 보가 설치되어 있어야함
        if (x>0 and mp[x-1][y][0]) or (x>0 and mp[x-1][y+1][0]) or (y>0 and mp[x][y-1][1] and mp[x][y+1][1]):
            return True
        else:
            return False


def solution(n, build_frame):
    # 교차점의 [0]은 기둥, [1]은 보
    mp = [[[0, 0] for i in range(n+2)] for i in range(n+2)]
    for y, x, a, b in build_frame:
        # 삭제 명령어일때
        if b == 0:
            # 그래프를 복사해서 해당 원소를 지워본 뒤
            tmp_mp = deepcopy(mp)
            tmp_mp[x][y][a] = False
            # validity를 체크한다
            # 삭제한게 기둥이라면, 양 옆에 보가 있거나 / 위에 기둥이 있다면 그들의 validity 체크
            if a == 0:
                result = 0
                if y > 0 and tmp_mp[x+1][y-1][1]:
                    tmp_mp[x+1][y-1][1] = 0
                    result += 1
                    if is_valid(x+1, y-1, tmp_mp, 1):
                        result -= 1
                if tmp_mp[x+1][y][1]:
                    result += 1
                    if is_valid(x+1, y, tmp_mp, 1):
                        result -= 1
                if tmp_mp[x+1][y][0]:
                    result += 1
                    if is_valid(x+1, y, tmp_mp, 0):
                        result -= 1
                if result == 0:
                    mp[x][y][a] = False
            # 삭제한게 보라면, 양 옆에 보가 있거나 / 그 자리 또는 x+1에 기둥이 있다면 그들의 validity 체크
            else:
                result = 0
                if y > 0 and tmp_mp[x][y-1][1]:
                    result += 1
                    if is_valid(x, y-1, tmp_mp, 1):
                        result -= 1
                if tmp_mp[x][y+1][1]:
                    result += 1
                    if is_valid(x, y+1, tmp_mp, 1):
                        result -= 1
                if tmp_mp[x][y][0]:
                    result += 1
                    if is_valid(x, y, tmp_mp, 0):
                        result -= 1
                if tmp_mp[x][y+1][0]:
                    result += 1
                    if is_valid(x, y+1, tmp_mp, 0):
                        result -= 1
                if result == 0:
                    mp[x][y][a] = False
        # 설치 명령어일때
        else:
            # validity를 체크해보고 가능하면 설치한다     
            if is_valid(x, y, mp, a):
                mp[x][y][a] = True
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            x, y = mp[i][j]
            if x:
                answer.append([j, i, 0])
            if y:
                answer.append([j, i, 1])
    answer.sort()
    print(answer)


solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
