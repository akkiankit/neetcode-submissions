class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i != j:
        #             prod *= nums[j]
        #     res[i] = prod
        # return res

        # prefix & suffix optimal
        n = len(nums)
        res = [1] * n
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
        return res 

        
        