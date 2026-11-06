class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = []
        for t in timePoints:
            h, m = t.split(":")
            mins.append(int(h) * 60 + int(m))
        mins.sort()
        d = abs(mins[-1] - mins[0])
        d = min(d, 1440 - d)
        res = d
        for i in range(len(mins) - 1):
            d = mins[i+1] - mins[i]
            res = min(res, d)
        return res
