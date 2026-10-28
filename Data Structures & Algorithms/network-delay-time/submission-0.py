class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        h = [(0, k)]
        d = {}
        while h:
            dd, u = heapq.heappop(h)
            if u in d:
                continue
            d[u] = dd
            for v, t in graph[u]:
                if v not in d:
                    heapq.heappush(h, (dd+t, v))
        return max(d.values()) if len(d) == n else -1