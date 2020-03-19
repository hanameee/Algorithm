def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True  # 기존 candidate 퀸 위치와 조건을 비교했을 때 아무 문제가 없다면 그 위치에 놓ㅇ르 수 있다는 것


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:  # 배치가 다 끝났다면
        final_result.append(current_candidate[:])  # 얇은 복사
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()  # pruning


def solve_n_queens(N):
    final_result = list()  # 최종 배치도는 리스트 형태로 저장
    DFS(N, 0, [], final_result)  # 초기 값은 아직 아무 퀸도 배치되지 않았으므로
    return final_result


print(solve_n_queens(4))
