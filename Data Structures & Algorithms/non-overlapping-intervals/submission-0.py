class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[1])
        removed = 0
        l_e = intervals[0][1]
        for s, e in intervals[1:]:
            if s < l_e:
                removed += 1
            else:
                l_e = e
        return removed