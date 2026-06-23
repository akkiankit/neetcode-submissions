class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])

                water_am = height * width
                if max_water < water_am:
                    max_water = water_am
        return max_water

























        # max_area = 0
        # for i in range(0, len(heights)):
        #     for j in range(i, len(heights)):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         area = width * height
        #         max_area = max(area, max_area)

        # return max_area

        # two pointer:
        # l = 0
        # r = len(heights) - 1
        # max_area = 0
        # while l < r:
        #     width = r - l
        #     height = min(heights[l], heights[r])
        #     area = width * height
        #     max_area = max(area, max_area)
        #     if heights[l] < heights[r]:
        #         l += 1
        #     else:
        #         r -=1
        # return max_area


     
        