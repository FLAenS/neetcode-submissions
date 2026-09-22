class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = (r - l) * min(heights[l], heights[r])
        while l < r:
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
        return res
