def solution(s):
    result = ""
    buff = ""
    for char in s:
        if char == " ":
            if len(buff) > 0:
                if len(buff) > 1:
                    result += buff[0].upper() + buff[1:].lower()
                else:
                    result += buff[0].upper()
            buff = ""
            result += " "
        else:
            buff += char
    if len(buff) > 1:
        result += buff[0].upper() + buff[1:].lower()
    elif len(buff) == 1:
        result += buff[0].upper()
    return result


print(solution(" 3people unFollowed me   "))
print(solution("3people   unFollowed me"))
