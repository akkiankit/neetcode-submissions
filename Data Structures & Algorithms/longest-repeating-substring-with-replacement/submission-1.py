class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1
            windowslength = r-l+1
            max_f = max(counter.values())
            if windowslength -  max_f <= k:
                if res < windowslength:
                    res = windowslength
            else:
                counter[s[l]] -= 1
                l += 1
                

        return res




            


        