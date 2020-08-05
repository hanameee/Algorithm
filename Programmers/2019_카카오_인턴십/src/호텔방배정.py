import sys
sys.setrecursionlimit(1e9)
next_room = dict()


def find_next(order, rooms):
    # 빈 방을 찾은 경우
    if order not in rooms:
        rooms[order] = order+1
        return order
    # 아닌 경우
    next_empty_room = find_next(rooms[order], rooms)
    rooms[order] = next_empty_room+1
    return next_empty_room


def solution(k, room_number):
    # 해당 방 번호보다 값이 크면서 빈 방 저장하는 dict
    rooms = dict()
    answer = []
    for order in room_number:
        next_empty_room = find_next(order, rooms)
        answer.append(next_empty_room)
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
