import re


def find_url(html):
    url_regex = re.compile(r'<meta[^>]+content="https:\/\/.+?\/>')
    match_obj = url_regex.search(html)
    if match_obj is None:
        return None
    target = match_obj.group()
    urlStart = target.find('content="https://') + 9
    urlEnd = target[urlStart:].find('"')
    return target[urlStart:urlStart+urlEnd]


def get_base_score(html, word):
    return re.subn(pattern="[^a-zA-Z]".format(word),
                   repl=' ', string=html.lower())


def get_link_count(html):
    return html.count("<a href=")


def solution(word, pages):
    url_arr = []
    base_score = []
    link_count = []
    link_score = [[] for _ in range(len(pages))]
    total_score = 0
    answer_idx = 0

    def get_connection(curr_idx):
        for idx in range(len(pages)):
            if idx != curr_idx:
                if url_arr[idx] != None:
                    url = '<a href="{}">'.format(url_arr[idx])
                    if pages[curr_idx].count(url) > 0:
                        link_score[idx].append(curr_idx)
    for page in pages:
        url_arr.append(find_url(page))
        link_count.append(get_link_count(page))
    for i in range(len(pages)):
        get_connection(i)
    for page in pages:
        replaced_page = get_base_score(page, word.lower())[0]
        replaced_page = replaced_page.split()
        base_score.append(replaced_page.count(word.lower()))

    for i in range(len(pages)):
        score = base_score[i]
        for link in link_score[i]:
            if link_count[link]:
                score += base_score[link]/link_count[link]
        if score > total_score:
            total_score = score
            answer_idx = i
    return answer_idx

solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\" rorororo/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
         )