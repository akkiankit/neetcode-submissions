class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r-l +1, res)
                total -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
        
        
        
        
        # s = sum(nums)
        # if s < target:
        #     return 0
        
        # m_l = float('inf')
        # for i in range(len(nums)):
        #     cur_s = 0
        #     for j in range(i, len(nums)):
        #         cur_s += nums[j]
        #         l = len(nums[i:j+1])
        #         # print(cur_s, l, nums[i:j+1])
        #         if cur_s >= target:
        #             if m_l > l:
        #                 m_l = l
        # return m_l
                