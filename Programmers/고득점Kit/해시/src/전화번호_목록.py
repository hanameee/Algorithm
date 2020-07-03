def solution(phone_book):
    sorted_book = sorted(phone_book)
    for idx in range(len(sorted_book)-1):
        print(sorted_book[idx], sorted_book[idx+1][:len(sorted_book[idx])])
        if sorted_book[idx] == sorted_book[idx+1][:len(sorted_book[idx])]:
            return "false"
    return "true"


# print(solution(["12", "123", "1235", "567", "88"]))
print(solution(["119", "97674223", "1195524421"]))
