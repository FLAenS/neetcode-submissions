class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(sub_nums: List[int]):
            prev2 = 0
            prev1 = 0
            for num in sub_nums:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(helper(nums[:-1]), helper(nums[1:]))