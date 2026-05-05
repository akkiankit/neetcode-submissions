class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_product = float('-inf')
        # for i in range(0, len(nums)):
        #     current_product = 1 
        #     for j in range(i, len(nums)):
        #         current_product *= nums[j]
               
        #         if current_product > max_product:
        #             max_product = current_product
            
        # return max_product

        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp_max = max(num, num * max_prod, num * min_prod)
            min_prod = min(num, num * max_prod, num * min_prod)
            max_prod = temp_max

            result = max(result, max_prod)
        return result

        