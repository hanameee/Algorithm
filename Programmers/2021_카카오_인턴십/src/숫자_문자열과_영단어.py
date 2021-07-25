number_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def isIntStr(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def isNumberStr(s):
    if s in number_dict.keys():
        return number_dict[s]
    else:
        return False


def solution(s):
    answer = ""
    buffer = ""
    for char in s:
        if isIntStr(char):
            answer += char
        else:
            buffer += char
        isNumber = isNumberStr(buffer)
        if isNumber:
            answer += isNumber
            buffer = ""
    return int(answer)
