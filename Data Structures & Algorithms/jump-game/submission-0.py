class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        for i, jump in enumerate(nums):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + jump)
        return True