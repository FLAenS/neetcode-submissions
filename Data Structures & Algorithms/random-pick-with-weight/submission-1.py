class Solution:

    def __init__(self, w: List[int]):
        self.rg = []
        self.wsum = sum(w)
        idx = 0
        for i in range(len(w)):
            self.rg.append(idx + w[i])
            idx += w[i]

    def pickIndex(self) -> int:
        rg = self.rg
        idx = random.randint(0, self.wsum - 1)
        l, r = 0, len(rg) - 1
        while l < r:
            mid = (l + r) // 2
            if rg[mid] > idx:
                r = mid
            else:
                l = mid + 1
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()