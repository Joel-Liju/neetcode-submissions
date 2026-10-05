class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        startIdx = -1
        endIdx = -1
        if len(intervals) == 0:
            return [newInterval]
        for i, interval in enumerate(intervals):
            # find start interval
            if interval[0] <= newInterval[0] <= interval[1]:
                startIdx = interval[0]
            if interval[0] <= newInterval[1] <= interval[1]:
                endIdx = interval[1]
            if i == 0:# very front
                if newInterval[0] < interval[0]:
                    startIdx = newInterval[0]
                if newInterval[1] < interval[0]:
                    endIdx = newInterval[1]
            if i == len(intervals) - 1:
                if interval[1] < newInterval[0]:
                    startIdx = newInterval[0]
                    endIdx = newInterval[1]
                if interval[1] < newInterval[1]:
                    endIdx = newInterval[1]
            if i > 0:
                prevInterval = intervals[i - 1]
                # print(prevInterval[1], interval[0])
                if prevInterval[1] < newInterval[0] < interval[0]:
                    startIdx = newInterval[0]
                if prevInterval[1] < newInterval[1] < interval[0]:
                    endIdx = newInterval[1]
        i = 0 
        while i < len(intervals):
            if endIdx < intervals[i][0]:
                break 
            if startIdx <= intervals[i][0] <= endIdx and startIdx <= intervals[i][1] <= endIdx:
                intervals.pop(i)
            else:
                i+=1
        
        intervals.insert(i, [startIdx, endIdx])

        return intervals