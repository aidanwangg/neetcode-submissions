"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            x = intervals[i]
            for j in range(i + 1, len(intervals)):
                y = intervals[j]
                if min(x.end, y.end) > max(x.start, y.start):
                    return False
        return True