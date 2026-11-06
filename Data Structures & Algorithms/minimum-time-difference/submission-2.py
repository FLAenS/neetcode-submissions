class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        seen = [False] * 1440
        for t in timePoints:
            m = int(t[:2]) * 60 + int(t[3:])
            if seen[m]:
                return 0
            seen[m] = True
        res = 1440
        first = prev = -1
        for m in range(1440):
            if seen[m]:
                if prev == -1:
                    first = m
                else:
                    res = min(res, m - prev)
                prev = m
        res = min(res, first + 1440 - prev)
        return res

