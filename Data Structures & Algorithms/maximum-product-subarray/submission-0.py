class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax = nums[0]
        curmin = nums[0]
        for num in nums[1:]:
            if num < 0:
                curmax, curmin = curmin, curmax
            curmax = max(num, curmax * num)
            curmin = min(num, curmin * num)
            res = max(res, curmax)
        return res