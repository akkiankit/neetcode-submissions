class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False

        dic_s = {}
        for char in s:
            if char in dic_s:
                dic_s[char] += 1
            else:
                dic_s[char] = 1
        
        dic_t = {}
        for char in t:
            if char in dic_t:
                dic_t[char] += 1
            else:
                dic_t[char] = 1

        if dic_s == dic_t:
            return True
        else:
            return False


        