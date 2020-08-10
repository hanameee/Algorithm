def solution(s):
    arr = s.split(" ")
    result = ""
    for idx in range(len(arr)):
        word = arr[idx]
        if word == "":
            result += " "
            continue
        if len(word) > 1:
            result += word[0].upper()+word[1:].lower()
        else:
            result += word[0].upper()
        if idx != len(arr)-1:
            result += " "
    return result


print(solution(" 3people unFollowed me"))
print(solution("3people   unFollowed me"))
