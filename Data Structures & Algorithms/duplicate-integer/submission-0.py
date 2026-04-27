class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        flag = False
        for value in dic.values():
            if value > 1:
                flag = True
                break
        return flag
        

        
        