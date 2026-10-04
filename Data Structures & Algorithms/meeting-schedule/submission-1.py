"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x : (x.start, x.end))
        start = None
        end = None
        for interval in intervals:
            if not start and not end:
                start = interval.start
                end = interval.end
            else:
                if start <= interval.start < end:
                    return False
                else:
                    start = interval.start
                    end = interval.end

        return True