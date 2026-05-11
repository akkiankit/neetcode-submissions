class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        # result = []
        # for interval in intervals:
        #     if not result:
        #         result.append(interval)
        #     else:
        #         last = result[-1]
        #         if interval[0] <= last[1]:
        #             last[1] = max(last[1], interval[1])
        #         else:
        #             result.append(interval)
        # return result
        intervals.sort(key=lambda x: x[0]) # O(nlogn)
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

 
