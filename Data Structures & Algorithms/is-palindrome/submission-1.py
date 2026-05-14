class Solution:
    def isPalindrome(self, s: str) -> bool:
        slower = ""
        for c in s:
            if c.lower() in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                slower +=c.lower()

        if slower[::] == slower[::-1]:
            return True
        else:
            return False