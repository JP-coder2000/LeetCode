def isPalindrome(string):
    slen = len(string)
    sliced = string[slen::-1]
    if sliced == string:
        return True
    else:
        return False
    pass
