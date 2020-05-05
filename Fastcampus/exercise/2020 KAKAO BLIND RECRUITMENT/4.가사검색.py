def solution(words, queries):
    words.sort()
    word_data = [[[], []]for _ in range(100001)]
    for word in range(len(words)):
        word_data[len(words[word])].append(words[word])
    answer = [0 for i in range(len(queries))]
    for qry_idx in range(len(queries)):
        qry = queries[qry_idx]
        sub_qry = ""
        # 쿼리에서 ?가 아닌 문자열 찾기
        for idx in range(len(qry)):
            if qry[idx] != "?":
                sub_qry += qry[idx]
            else:
                # 연속된 ?가 아니라면
                if sub_qry:
                    break
        sub_qry_idx = qry.find(sub_qry[0])
        # query 길이와 같은 후보 단어들에 대해
        if sub_qry_idx == 0:  # 앞에서부터 정렬된 애를 써야함
            for word in word_data[len(qry)]:
                if word[sub_qry_idx:sub_qry_idx+len(sub_qry)] == sub_qry:
                    answer[qry_idx] += 1
                else:
                    # 정렬되어 있으므로 더이상 아니라면 없는 것
                    if(answer[qry_idx]):
                        break
        else:
            for word in word_data[len(qry)]:
                if word[sub_qry_idx:sub_qry_idx+len(sub_qry)] == sub_qry:
                    answer[qry_idx] += 1
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
      "fro??", "????o", "fr???", "fro???", "pro?"]))
