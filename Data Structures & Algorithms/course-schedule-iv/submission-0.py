class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # take a then take b, a is pre for b, asking if u is pre for v
        g = defaultdict(list)
        ind = [0] * numCourses
        pre = defaultdict(set)
        for a, b in prerequisites:
            g[a].append(b)
            ind[b] += 1
        q = deque([i for i in range(numCourses) if ind[i] == 0])
        while q:
            cur = q.popleft()
            for nxt in g[cur]:
                pre[nxt].add(cur)
                pre[nxt].update(pre[cur])
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
        return [u in pre[v] for u, v in queries]
