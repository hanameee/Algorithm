import math


def get_y(x, w, h):
    return -(h/w)*x+h


def solution(w, h):
    answer = w*h
    prev_y = get_y(0, w, h)
    if w % 2 == 1:
        for i in range((w//2)):
            next_y = get_y(i+1, w, h)
            answer -= 2*(math.ceil(prev_y)-math.floor(next_y))
            prev_y = next_y
        answer -= math.ceil(get_y(w//2, w, h)) - \
            math.floor(get_y((w//2)+1, w, h))
    else:
        for i in range(w//2):
            next_y = get_y(i+1, w, h)
            answer -= 2*(math.ceil(prev_y)-math.floor(next_y))
            prev_y = next_y
    return answer


print(solution(2, 7))  # 80
