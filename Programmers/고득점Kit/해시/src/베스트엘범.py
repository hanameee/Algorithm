def solution(genres, plays):
    genre_list = []
    genre_count = []
    genre_play = []
    for idx in range(len(genres)):
        if genres[idx] in genre_list:
            genre_idx = genre_list.index(genres[idx])
            genre_count[genre_idx] += plays[idx]
            genre_play[genre_idx].append((idx, plays[idx]))
        else:
            genre_list.append(genres[idx])
            genre_count.append(plays[idx])
            genre_play.append([(idx, plays[idx])])
    enumerated_genre = list(enumerate(genre_count))
    enumerated_genre.sort(key=lambda x: -x[1])
    answer = []
    for i in range(len(genre_list)):
        curr_genre = enumerated_genre[i][0]
        sorted_genre_play = sorted(
            genre_play[curr_genre], key=lambda x: (-x[1], x[0]))
        if len(sorted_genre_play) > 1:
            for j in range(2):
                answer.append(sorted_genre_play[j][0])
        else:
            answer.append(sorted_genre_play[0][0])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))
