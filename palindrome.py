def is_palindrome(word):
    for left in range(int(len(word)/2)):
        temp = 0
        if word[left] != word[len(word)-1-left]:
            temp += 1 
    if temp > 0:
        return False
    else:
        return True
    

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))