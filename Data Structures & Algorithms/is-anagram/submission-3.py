class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # if s==t:
        #     return True
        # else:
        #     return False
        counter_s = {}
        for char in s:
            if char in counter_s:
                counter_s[char] += 1
            else:
                counter_s[char] = 1

        counter_t = {}
        for char in t:
            if char in counter_t:
                counter_t[char] += 1
            else:
                counter_t[char] = 1
        if counter_s == counter_t:
            return True
        else:
            return False



        