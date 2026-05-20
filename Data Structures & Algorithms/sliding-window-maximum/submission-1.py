class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums)-k+1):
            suba = nums[i:i+k]
            res.append(max(suba))
        return res
        