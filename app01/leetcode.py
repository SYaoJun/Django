class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lst = ""
        for c in s:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
                lst += c
        return lst == lst[::-1]
