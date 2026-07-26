class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                w = j - i
                h = min(heights[i], heights[j])
                a = w * h
                ans = max(ans, a)
        return ans
        