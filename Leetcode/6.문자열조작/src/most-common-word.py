from collections import Counter


def solution(paragraph, banned):
    paragraph = paragraph.lower()
    filtered_paragraph = ""
    buf = ""
    for char in paragraph:
        if char.isalpha():
            filtered_paragraph += char
            continue
        filtered_paragraph += " "
    arr = list(map(lambda x: x.lower(), filtered_paragraph.split()))
    filtered_arr = []
    for item in arr:
        if item not in banned:
            filtered_arr.append(item)
    c = Counter(filtered_arr)
    return c.most_common(1)[0][0]


print(
    solution("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(
    solution(
        "a, a, a, a, b,b,b,c, c", ["a"]))
