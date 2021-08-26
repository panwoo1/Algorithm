def is_palindrome(word):
    if(len(word) < 2):
        return True
    if(word[0] != word[-1]):
        return False
    return is_palindrome(word[1:-1])


'''
수행시간 점화식
T(n) = T(n-2) + c       ##3아마 이거인듯
T(n) = T(n/2) + c    

둘중 하나
'''