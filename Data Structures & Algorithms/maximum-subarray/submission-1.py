class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        for i in range(n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)