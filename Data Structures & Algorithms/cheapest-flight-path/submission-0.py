class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        for i in range(k + 1):
            tmp = dist[:]
            for u, v, price in flights:
                if dist[u] != INF:
                    tmp[v] = min(tmp[v], dist[u] + price)
            dist = tmp
        return dist[dst] if dist[dst]!=INF else -1