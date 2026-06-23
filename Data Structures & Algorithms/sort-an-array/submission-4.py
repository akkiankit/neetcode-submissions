class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
        # Bubble sort
        # for i in range(len(nums) - 1):
        #     swapped = False
        #     for j in range(len(nums) - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             swapped = True
        #     if not swapped:
        #         break
        # return nums

        # # selection sort
        # for i in range(len(nums)):
        #     min_index = i
        #     for j in range(i+1, len(nums)):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     if min_index != i:
        #         nums[i], nums[min_index] = nums[min_index], nums[i]
        # return nums

        # # Insertion Sort
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

        return nums

                

         

        