class Solution:
    def isValid(self, s: str) -> bool:
        # Brute force - we need to replace the valid pair with '' 
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('[]','')
            s = s.replace('()', '')
            s = s.replace('{}', '')
        return s == ''
        