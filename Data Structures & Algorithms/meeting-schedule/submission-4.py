"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x : x.start)

        if len(intervals) == 0:
            return True

        must_be_done = intervals[0].end

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end

            if must_be_done > start:
                return False

            must_be_done = end

        return True