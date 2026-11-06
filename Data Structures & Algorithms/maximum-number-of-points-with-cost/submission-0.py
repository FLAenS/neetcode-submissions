class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        prev = points[0][:]
        for i in range(1, rows):
            left = [0] * cols
            right = [0] * cols

            left[0] = prev[0]
            for j in range(1, cols):
                left[j] = max(left[j - 1] - 1, prev[j])
            right[cols - 1] = prev[cols - 1]
            for j in range(cols - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev[j])
            for j in range(cols):
                prev[j] = points[i][j] + max(left[j], right[j])
        return max(prev)