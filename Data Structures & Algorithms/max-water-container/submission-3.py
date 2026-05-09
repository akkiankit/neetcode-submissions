class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0
        # for i in range(0, len(heights)):
        #     for j in range(i, len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         area = width * height
        #         max_area = max(area, max_area)

        # return max_area

        # two pointer:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return max_area


     
        