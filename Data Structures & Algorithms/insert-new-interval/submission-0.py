class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # O(nlogn)
        complete_interval = intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            outputEnd = output[-1][1]
            if start <= outputEnd:
                output[-1][1] = max(outputEnd, end)
            else:
                output.append([start,end])
        return output
        