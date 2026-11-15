class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # find a node, edge number == n - 1, and it doesnt go out
        graph = defaultdict(list)
        seen = set()
        for a, b in trust:
            graph[b].append(a)
            seen.add(a)
        for i in range(1, n + 1):
            if len(graph[i]) == n - 1:
                if i not in seen:
                    return i
        return -1