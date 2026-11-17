class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for s, e in intervals[1:]:
            olds, olde = res[-1][0], res[-1][1]
            if s <= olde:
                if e > olde:
                    res[-1][1] = e
            else:
                res.append([s, e])
        return res