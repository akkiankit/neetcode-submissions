class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            res[i] = prod
        return res

        # 1, 2, 3, 4

        # cur = 1
        # 1, 1, 1
        # 1, 2, 2*1 = 2
        # 1, 3, 2 *3 = 6
        # 1, 4, 6*4 = 24
        # [24,]
        # 2, 1, 1*2 = 2
        # 2, 2, 2 * 2 = 4
        # 2, 3 ,  4 * 3 = 12
        