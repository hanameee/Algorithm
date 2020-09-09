def solution(files):
    file_arr = []
    for file in files:
        result = [file]
        cur_idx = 0
        head_idx = 0
        num_idx = 0
        for idx in range(0, len(file)):
            if 48 <= ord(file[idx]) <= 57:
                cur_idx = idx
                head_idx = idx
                break
        result.append(file[0:cur_idx].lower())
        for idx in range(head_idx, len(file)):
            cur_idx = idx + 1
            if ord(file[idx]) < 48 or ord(file[idx]) > 57:
                cur_idx = idx
                num_idx = idx
                break
            if int(file[head_idx:idx+1]) > 99999:
                cur_idx = idx
                num_idx = idx
                break
        result.append(int(file[head_idx:cur_idx]))
        file_arr.append(result)
    file_arr.sort(key=lambda x: [x[1], x[2]])
    result = []
    for sortedFile in file_arr:
        result.append(sortedFile[0])
    return result
