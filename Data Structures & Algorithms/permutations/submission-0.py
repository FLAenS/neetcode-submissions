class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []
        n = len(nums)
        used = [False] * n 
        def dfs():
            if len(cur) == n:
                res.append(cur[:])
                return
            for i in range(n):
                if not used[i]:
                    cur.append(nums[i])
                    used[i] = True
                    dfs()
                    cur.pop()
                    used[i] = False
        dfs()
        return res