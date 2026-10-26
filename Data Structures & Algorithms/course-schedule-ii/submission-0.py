class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return res if len(res) == numCourses else []