class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        counter = 0
        endVal = intervals[0][1]

        for i in range(1, len(intervals)):
            if endVal <= intervals[i][0]:#non overlapping case
                endVal = intervals[i][1]
            else:
                # overlapping case
                endVal = min(intervals[i][1], endVal)
                counter += 1
        return counter