def get_target_position(target):
    if target == 0:
        return [3, 1]
    else:
        return [(target-1)//3, (target-1) % 3]


def solution(numbers, hand):
    left_position = [3, 0]
    right_position = [3, 2]
    answer = ''
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left_position = get_target_position(num)
        elif num in [3, 6, 9]:
            answer += "R"
            right_position = get_target_position(num)
        else:
            target_position = get_target_position(num)
            left_diff = abs(
                left_position[0]-target_position[0]) + abs(left_position[1]-target_position[1])
            right_diff = abs(
                right_position[0]-target_position[0]) + abs(right_position[1]-target_position[1])
            if left_diff < right_diff:
                answer += "L"
                left_position = target_position
            elif left_diff > right_diff:
                answer += "R"
                right_position = target_position
            else:
                if hand == "left":
                    answer += "L"
                    left_position = target_position
                else:
                    answer += "R"
                    right_position = target_position
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
# LRLLRRLLLRR
