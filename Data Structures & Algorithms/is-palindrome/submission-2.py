class Solution:
    def isPalindrome(self, s: str) -> bool:
        # slower = ""
        # for c in s:
        #     if c.lower() in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
        #         slower +=c.lower()

        # if slower[::] == slower[::-1]: # space complexity is O(n)
        #     return True
        # else:
        #     return False
        # here time complexity is o(n) and spece complexity is also o(n)
        # print(ord('a'), ord('z'), ord('0'), ord('9'), ord('A'), ord('Z'))
        # 97 122 48 57 65 90
        l = 0
        r = len(s) - 1
        while l < r:

            while l < r and not ( (97 <= ord(s[l].lower()) <= 122) or (48 <= ord(s[l].lower()) <=57 )):
                l += 1
            
            while r > l and not ( (97 <= ord(s[r].lower()) <= 122) or (48 <= ord(s[r].lower()) <=57 )):
                r -= 1

           
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        return True

