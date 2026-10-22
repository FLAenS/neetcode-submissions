class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        h = [-c for c in cnt.values()]
        heapq.heapify(h)
        cooldown = deque()
        time = 0
        while h or cooldown:
            time += 1
            if h:
                c = heapq.heappop(h) + 1
                if c != 0:
                    cooldown.append([c, time + n])
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(h, cooldown.popleft()[0])
        return time