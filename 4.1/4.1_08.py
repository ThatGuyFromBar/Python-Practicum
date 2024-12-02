def is_palindrome(s):
    if isinstance(s, int):
        s = str(abs(s))
    return s == s[::-1]
