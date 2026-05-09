class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(0, len(heights)):
            for j in range(i, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height
                max_area = max(area, max_area)

        return max_area
     
        