class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # out = []
        # for i in range(0, len(nums)):
        #     product =1
        #     for j in range(0, len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     out.append(product)
        # return out
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result           


        