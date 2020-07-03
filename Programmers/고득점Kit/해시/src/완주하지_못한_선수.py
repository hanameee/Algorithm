def solution(participant, completion):
    participant_dict = {}
    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
    for c in completion:
        participant_dict[c] -= 1
    for p in participant_dict:
        if participant_dict[p] == 1:
            return p


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["marina", "josipa", "nikola", "filipa"]))
