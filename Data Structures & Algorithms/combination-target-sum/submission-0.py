class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base condition
            if total == target:
                res.append(list(cur))
                return 
            
            if i >= len(nums) or total > target:
                return 

            # choose
            cur.append(nums[i])

            # explore
            dfs(i, cur, total + nums[i])

            # unchoose
            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


            

        
        