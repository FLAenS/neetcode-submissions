class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1.0/val))
        def bfs(s, e):
            if s not in graph or e not in graph:
                return -1.0
            if s == e:
                return 1.0
            q = deque([(s, 1.0)])
            v = {s}
            while q:
                cur, val = q.popleft()
                if cur == e:
                    return val
                for nxt, weight in graph[cur]:
                    if nxt not in v:
                        v.add(nxt)
                        q.append((nxt, val * weight))
            return -1.0
        return [bfs(a, b) for a, b in queries]