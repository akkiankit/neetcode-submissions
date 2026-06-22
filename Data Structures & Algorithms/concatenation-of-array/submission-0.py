class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        answer.extend(nums)
        answer.extend(nums)
        return answer

        