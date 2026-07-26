class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countS = {}
        l = 0
        r = 0
        mlen = 0
        freq = 0
        while r < len(s):
            countS[s[r]] = countS.get(s[r], 0) + 1
            freq = max(countS.get(s[r], 0), freq)
            window = r - l + 1
            if window - freq > k:
                countS[s[l]] -= 1
                l += 1
            mlen = max(mlen, r - l + 1)
            r += 1
        return mlen

# loop 4 : r = 3, l = 0, freq = 3, mlen = 4, windo = 4 , window-freq > k: 1> 1 
# loop 5: r = 4, l = 0, freq = 4, 5-4 > 1, mlen = 5
# loop 6: r = 5, l = 0, freq = 4, 6-4 > 1 