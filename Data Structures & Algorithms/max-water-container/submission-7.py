class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        l, r = 0 , len(heights) - 1
        res = 0 
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res


        # ans = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         w = j - i
        #         h = min(heights[i], heights[j])
        #         a = w * h
        #         ans = max(ans, a)
        # return ans
        