class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        ind = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            ind[a]+=1
        q = deque([i for i in range(numCourses) if ind[i] == 0])
        c = set()
        while q:
            cur = q.popleft()
            c.add(cur)
            for nxt in graph[cur]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
        return len(c) == numCourses