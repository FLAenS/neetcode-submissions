class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum = -1, float('-inf')
        for num in nums:
            if cursum > 0:
                cursum += num
            else:
                cursum = num
            maxsum = max(maxsum, cursum)

        return maxsum
