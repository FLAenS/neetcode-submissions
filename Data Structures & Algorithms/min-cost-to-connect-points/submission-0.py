class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        h = [(0, 0)]
        total = 0
        while h:
            cost, i = heapq.heappop(h)
            if i in visited:
                continue
            visited.add(i)
            total += cost
            x, y = points[i]
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    cost = abs(x - xj) + abs(y - yj)
                    heapq.heappush(h, (cost, j))
        return total 

