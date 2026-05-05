class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        for i in range(0, len(nums)):
            current_product = 1 
            for j in range(i, len(nums)):
                current_product *= nums[j]
               
                if current_product > max_product:
                    max_product = current_product
            
        return max_product

        