def is_palindrome(word):
    for left in range(int(len(word)/2)):
        right = len(word)-1-left
    if word[left] == word[right]:
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))