def checkMagazine(magazine, note):
    word_dict = {}
    for word in magazine:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for word in note:
        if word in word_dict:
            if word_dict[word] == 0:
                return "No"
            word_dict[word] -= 1
        else:
            return "No"
    return "Yes"
