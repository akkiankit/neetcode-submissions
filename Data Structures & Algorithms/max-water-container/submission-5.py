class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_water = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])

        #         water_am = height * width
        #         if max_water < water_am:
        #             max_water = water_am
        # return max_water
        # # Two pointer approach:
        l, r = 0 , len(heights) -1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r-l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res



     
        