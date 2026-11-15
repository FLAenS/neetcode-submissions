class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        v = set(["0000"])
        q = deque([("0000", 0)])
        while q:
            cur, step = q.popleft()
            if cur == target:
                return step
            for i in range(4):
                n = int(cur[i])
                for move in (1, -1):
                    new = (n + move) % 10
                    nxt = cur[:i] + str(new) + cur[i + 1:]

                    if nxt not in v and nxt not in dead:
                        v.add(nxt)
                        q.append((nxt, step+1))
        return -1
