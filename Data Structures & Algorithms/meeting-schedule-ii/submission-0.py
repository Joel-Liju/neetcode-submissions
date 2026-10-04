"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        counter = 0
        maxCounter = 0

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start = sorted(start)
        end = sorted(end)

        sP, rP = 0, 0

        while sP < len(start) or rP < len(end):
            if sP < len(start):
                if start[sP] < end[rP]:
                    counter += 1
                    sP += 1
                else:
                    rP += 1
                    counter -= 1
            else:
                counter -= 1
                rP += 1
            maxCounter = max(counter, maxCounter)
        return maxCounter