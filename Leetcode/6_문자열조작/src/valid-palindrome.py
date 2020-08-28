def isPalindrome(s):
    filtered_str = ""
    s = s.lower()
    for char in s:
        if char.isalnum():
            filtered_str += char
    if filtered_str == filtered_str[::-1]:
        return True
    else:
        return False


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome('0P'))
