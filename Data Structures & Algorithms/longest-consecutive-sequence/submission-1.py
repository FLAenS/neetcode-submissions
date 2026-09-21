class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        res = 0
        for n in nSet:
            if (n - 1) not in nSet:
                length = 1
                while (n + length) in nSet:
                    length += 1
                res = max(res, length)
        return res